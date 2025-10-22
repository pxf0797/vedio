"""
YouTube视频下载工具 - 增强版
支持YouTube视频签名提取失败情况的处理
提供更灵活的格式选择和错误处理
添加YouTube认证功能，解决"您不是机器人"验证问题

使用方法:
1. 运行脚本: python video.py
2. 输入YouTube视频链接
3. 根据提示选择验证方式
4. 选择清晰度或格式
5. 等待下载完成

更新日志:
- 增加了对YouTube签名提取失败的处理
- 添加了格式列表显示功能
- 支持自定义格式ID输入
- 改进了错误处理和用户提示
- 优化了下载参数配置
- 增加YouTube认证功能，解决"您不是机器人"验证问题
- 优化了多种错误的处理和重试机制
- 增强了网络问题的容错能力
"""
import os
import re
import yt_dlp
from datetime import datetime
import sys

# 检查yt-dlp版本
try:
    yt_dlp_version = yt_dlp.version.__version__
    print(f"当前yt-dlp版本: {yt_dlp_version}")
    print("更新yt-dlp版本使用指令: pip install -U yt-dlp")
    print("如遇到'您不是机器人'问题，请使用浏览器Cookie认证")
    # 如果版本过旧，提示更新
    if yt_dlp_version < "2025":
        print("⚠️ 您的yt-dlp版本可能较旧，建议更新: pip install -U yt-dlp")
except:
    print("⚠️ 无法检测yt-dlp版本")

def sanitize_filename(name: str) -> str:
    """
    去除文件名中不适合使用的特殊字符（跨平台处理）。
    以防止在 Windows/Mac/Linux 下可能出现的非法字符问题。
    """
    return re.sub(r'[\\/:*?"<>|]', '_', name).strip()

def setup_authentication(force_auth=False):
    """
    设置YouTube视频下载认证
    参数:
      force_auth (bool): 是否强制要求认证（当出现机器人检测时）
    返回:
      auth_opts (dict): 认证相关的yt-dlp选项
    """
    auth_opts = {}
    
    print("\n===== YouTube认证设置 =====")
    if force_auth:
        print("⚠️ YouTube检测到机器人行为，必须提供认证才能下载")
        print("⚠️ 您需要登录过YouTube的浏览器才能提取有效cookies")
    print("YouTube需要认证以确认您不是机器人。请选择认证方式:")
    print("1. 使用已有的cookies.txt文件 (如果存在)")
    print("2. 从浏览器中提取cookies (推荐)")
    print("3. 指定自定义cookie文件路径")
    print("4. 跳过认证 (可能无法下载部分视频)")
    
    choice = input("请输入选项 [1-4]: ").strip()
    
    if choice == '1':
        if os.path.exists('cookies.txt'):
            auth_opts['cookiefile'] = 'cookies.txt'
            print("将使用当前目录下的cookies.txt文件")
        else:
            print("当前目录下不存在cookies.txt文件，将从浏览器提取cookies")
            browsers = ["chrome", "firefox", "edge", "safari", "opera", "brave", "chromium"]
            print("可用的浏览器选项:")
            for i, browser_option in enumerate(browsers, 1):
                print(f"{i}. {browser_option}")
            browser_choice = input("请选择浏览器类型 [1-7]: ").strip()
            try:
                browser_idx = int(browser_choice) - 1
                if 0 <= browser_idx < len(browsers):
                    browser = browsers[browser_idx]
                    auth_opts['cookiesfrombrowser'] = (browser, None, None, None)
                    print(f"将从{browser}浏览器提取cookies")
                else:
                    print("无效选择，使用默认浏览器(chrome)")
                    auth_opts['cookiesfrombrowser'] = ("chrome", None, None, None)
            except ValueError:
                print("无效输入，使用默认浏览器(chrome)")
                auth_opts['cookiesfrombrowser'] = ("chrome", None, None, None)
    
    elif choice == '2':
        browsers = ["chrome", "firefox", "edge", "safari", "opera", "brave", "chromium"]
        print("可用的浏览器选项:")
        for i, browser_option in enumerate(browsers, 1):
            print(f"{i}. {browser_option}")
        browser_choice = input("请选择浏览器类型 [1-7]: ").strip()
        try:
            browser_idx = int(browser_choice) - 1
            if 0 <= browser_idx < len(browsers):
                browser = browsers[browser_idx]
                auth_opts['cookiesfrombrowser'] = (browser, None, None, None)
                print(f"将从{browser}浏览器提取cookies")
            else:
                print("无效选择，使用默认浏览器(chrome)")
                auth_opts['cookiesfrombrowser'] = ("chrome", None, None, None)
        except ValueError:
            print("无效输入，使用默认浏览器(chrome)")
            auth_opts['cookiesfrombrowser'] = ("chrome", None, None, None)
    
    elif choice == '3':
        custom_path = input("请输入cookie文件的完整路径: ").strip()
        if os.path.exists(custom_path):
            auth_opts['cookiefile'] = custom_path
            print(f"将使用{custom_path}作为cookie文件")
        else:
            print(f"文件{custom_path}不存在，将跳过认证")
    
    elif choice == '4':
        if force_auth:
            print("⚠️ 当前视频需要认证，跳过认证可能导致无法下载")
            confirm = input("确定要跳过认证吗？(y/n): ").strip().lower()
            if confirm != 'y':
                # 用户不想跳过认证，递归调用选择其他方式
                return setup_authentication(force_auth)
        print("已选择跳过认证，某些视频可能无法下载")
    
    else:
        print("无效选项，将尝试使用默认认证方式")
        if os.path.exists('cookies.txt'):
            auth_opts['cookiefile'] = 'cookies.txt'
            print("将使用当前目录下的cookies.txt文件")
    
    return auth_opts

def parse_formats(page_url: str):
    """
    使用 yt-dlp 提取视频信息，包括标题和所有可用格式。
    返回:
      title (str): 视频标题（若无则空字符串）
      formats (list): 所有可用的格式信息，每个元素是一个 dict
      auth_opts (dict): 认证选项，便于后续使用
    """
    # 获取认证选项
    auth_opts = setup_authentication()
    
    # 只解析、不下载
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        **auth_opts  # 添加认证选项
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(page_url, download=False)
    except Exception as e:
        error_str = str(e)
        if "Sign in to confirm you're not a bot" in error_str or "确认你不是机器人" in error_str:
            print("\n⚠️ YouTube检测到机器人行为，需要认证才能继续")
            # 强制要求认证
            auth_opts = setup_authentication(force_auth=True)
            ydl_opts.update(auth_opts)
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(page_url, download=False)
        else:
            raise  # 重新抛出其他类型的异常
    
    title = info.get("title") or ""
    formats = info.get("formats", [])
    return title, formats, auth_opts  # 返回认证选项以便后续使用

def categorize_formats(formats):
    """
    根据 formats 列表，将其分为:
      single_map: {height -> (format_id)}  # 同时包含视频+音频的单文件
      video_map:  {height -> (format_id)}  # 视频流
      audio_list: [(abr, format_id)]       # 音频流(不区分height, 常用abr排序)
    height 一般以 f["height"] 表示，若无则默认0
    
    返回: single_map, video_map, audio_list
    """
    single_map = {}
    video_map = {}
    audio_list = []

    for f in formats:
        format_id = f.get('format_id', '')
        vcodec = f.get('vcodec', 'none')
        acodec = f.get('acodec', 'none')
        height = f.get('height', 0) or 0  # 有的可能None

        # 判断是否有视频和音频
        has_video = (vcodec != 'none')
        has_audio = (acodec != 'none')

        if has_video and has_audio:
            # 单文件包含音画
            single_map[height] = format_id
        elif has_video and not has_audio:
            # 纯视频流
            video_map[height] = format_id
        elif not has_video and has_audio:
            # 纯音频流
            # 常用 abr(音频码率) 来区分好坏
            abr = f.get('abr', 0)
            audio_list.append((abr, format_id))

    # 按 abr 大小对 audio_list 排序，码率大的音质可能更好
    audio_list.sort(key=lambda x: x[0], reverse=True)

    return single_map, video_map, audio_list

def pick_resolution(single_map, video_map):
    """
    综合 single_map 和 video_map 的 height，按从大到小排序，供用户选择。
    返回: sorted_heights (list)
    """
    all_heights = set(single_map.keys()) | set(video_map.keys())
    all_heights = [h for h in all_heights if h > 0]  # 排除可能出现的0
    sorted_heights = sorted(all_heights, reverse=True)
    return sorted_heights

def multi_round_download(page_url, ydl_opts, auth_opts=None, max_rounds=3, max_retries=3):
    """
    以多轮、每轮多次重试的方式调用 yt-dlp 下载。
    - max_rounds: 最多轮数
    - max_retries: 每轮尝试次数 (在 yt-dlp 里一般只有一次下载机会，出错就需要下一轮)
    
    当出现下载错误时，允许用户输入 y/n 决定是否继续下一轮。
    针对HTTP 403错误提供特殊处理和格式回退选项。
    """
    # 可在HTTP 403错误时尝试的备选格式
    fallback_formats = [
        'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'bestvideo+bestaudio/best',
        'b/w',  # worst quality as last resort
    ]
    current_format_index = -1  # 用于跟踪当前使用的fallback_formats索引
    
    for round_idx in range(1, max_rounds + 1):
        for retry_idx in range(1, max_retries + 1):
            print(f"\n----- 第 {round_idx} 轮, 第 {retry_idx} 次尝试下载 -----")
            try:
                # 尝试使用当前的配置下载
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([page_url])
                return True
                
            except yt_dlp.networking.exceptions.HTTPError as http_err:
                # 针对HTTP 403 Forbidden错误的特殊处理
                if '403' in str(http_err):
                    print(f"遇到HTTP 403错误: {http_err}")
                    
                    # 尝试修改格式字符串
                    if current_format_index < len(fallback_formats) - 1:
                        current_format_index += 1
                        new_format = fallback_formats[current_format_index]
                        print(f"尝试使用备选格式: {new_format}")
                        ydl_opts['format'] = new_format
                        
                        # 禁用可能导致问题的设置
                        if retry_idx > 1:
                            # 尝试禁用代理
                            if ydl_opts.get('proxy'):
                                print("尝试禁用代理...")
                                ydl_opts['proxy'] = None
                            
                            # 修改User-Agent
                            print("尝试修改User-Agent...")
                            ydl_opts['http_headers']['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15'
                        
                        # 立即尝试新的配置
                        continue
                    else:
                        print("已尝试所有备选格式，仍然失败")
                        
                print(f"下载出错: {http_err}")
                
            except yt_dlp.utils.ExtractorError as e:
                # 这是格式问题，尝试使用列出格式后再选择
                if "Requested format is not available" in str(e) and retry_idx == 1:
                    print(f"请求的格式不可用，尝试列出所有格式并重新选择...")
                    try:
                        # 修改选项来列出所有格式
                        list_opts = ydl_opts.copy()
                        list_opts['listformats'] = True
                        list_opts['quiet'] = False
                        with yt_dlp.YoutubeDL(list_opts) as ydl_list:
                            ydl_list.download([page_url])
                        
                        # 当用户查看完可用格式后，让他们选择
                        format_id = input("\n请从上方列表中选择一个可用的格式ID: ").strip()
                        if format_id:
                            # 使用用户选择的格式ID
                            ydl_opts['format'] = format_id
                            # 直接尝试使用新格式下载
                            with yt_dlp.YoutubeDL(ydl_opts) as ydl_new:
                                ydl_new.download([page_url])
                            return True
                    except Exception as list_err:
                        print(f"尝试列出格式失败: {list_err}")
                # 检查是否是YouTube机器人检测问题
                error_str = str(e)
                if "Sign in to confirm you're not a bot" in error_str or "确认你不是机器人" in error_str:
                    print("\n⚠️ YouTube检测到机器人行为，需要认证才能继续")
                    print("正在尝试重新设置认证...")
                    
                    # 强制要求认证
                    new_auth_opts = setup_authentication(force_auth=True)
                    if new_auth_opts:
                        # 更新选项
                        ydl_opts.update(new_auth_opts)
                        if auth_opts is not None:
                            auth_opts.update(new_auth_opts)  # 更新外部的auth_opts以便后续使用
                        print("认证已更新，正在重试下载...")
                        continue
                    
                print(f"下载出错: {e}")
                
            except Exception as e:
                error_str = str(e)
                if "Sign in to confirm you're not a bot" in error_str or "确认你不是机器人" in error_str:
                    print("\n⚠️ YouTube检测到机器人行为，需要认证才能继续")
                    print("正在尝试重新设置认证...")
                    
                    # 强制要求认证
                    new_auth_opts = setup_authentication(force_auth=True)
                    if new_auth_opts:
                        # 更新选项
                        ydl_opts.update(new_auth_opts)
                        if auth_opts is not None:
                            auth_opts.update(new_auth_opts)  # 更新外部的auth_opts以便后续使用
                        print("认证已更新，正在重试下载...")
                        continue
                
                print(f"下载出错: {e}")
                
                # 如果是网络相关错误，尝试禁用代理
                if "urlopen error" in str(e) and ydl_opts.get('proxy') and retry_idx == max_retries:
                    print("尝试禁用代理并重试...")
                    ydl_opts['proxy'] = None
                    # 立即重试
                    continue

        # 当一轮尝试都失败时
        if round_idx < max_rounds:
            # 重置某些设置以提高下一轮的成功率
            if 'downloader' in ydl_opts and ydl_opts['downloader'] == 'aria2c':
                print("尝试使用原生下载器...")
                ydl_opts['downloader'] = None
                ydl_opts['downloader_args'] = {}
            
            cont = input("本轮失败，是否继续下一轮下载？(y/n): ").strip().lower()
            if cont != 'y':
                print("已终止下载流程。")
                return False
        else:
            print("已达到最大轮数，仍然全部失败。")
            return False

def main():
    page_url = input("请输入要下载的视频链接: ").strip()
    if not page_url:
        print("未输入链接，程序退出。")
        return

    # 1. 解析
    print("\n正在解析视频信息...")
    title_raw, formats, auth_opts = parse_formats(page_url)
    title_clean = sanitize_filename(title_raw)
    if not title_clean:
        # 若无标题，用日期时间表示
        title_clean = datetime.now().strftime('%Y%m%d_%H%M%S')

    # 2. 分类不同格式
    single_map, video_map, audio_list = categorize_formats(formats)

    # 如果所有 map 都为空，说明拿不到可下载的格式
    if not single_map and not video_map:
        print("未获取到标准格式，尝试使用yt-dlp默认下载方式...")
        
        # 询问是否需要自定义文件名
        custom_filename = input("\n是否需要自定义文件名？(y/n，默认n): ").strip().lower()
        if custom_filename == 'y':
            custom_name = input("请输入自定义文件名: ").strip()
            if custom_name:
                # 使用自定义名称
                title_clean = sanitize_filename(custom_name)
        
        ydl_opts = {
            'outtmpl': os.path.join('./download', f'{title_clean}.%(ext)s'),
            'format': 'best',
            'merge_output_format': 'mp4',
            **auth_opts  # 添加认证选项
        }
        success = multi_round_download(page_url, ydl_opts, max_rounds=3, max_retries=3)
        if success:
            print("\n下载完成！请查看下载文件夹：./download")
        else:
            print("\n下载未完成，请检查网络或重试")
        return

    # 3. 列出所有可用分辨率(从高到低)
    sorted_heights = pick_resolution(single_map, video_map)
    if not sorted_heights:
        # 如果在 single_map/video_map 中都没有 height>0
        print("未检测到可识别的分辨率，无法选择。尝试直接使用 yt-dlp 'best' 下载。")
        
        # 询问是否需要自定义文件名
        custom_filename = input("\n是否需要自定义文件名？(y/n，默认n): ").strip().lower()
        if custom_filename == 'y':
            custom_name = input("请输入自定义文件名: ").strip()
            if custom_name:
                # 使用自定义名称
                title_clean = sanitize_filename(custom_name)
                
        ydl_opts = {
            'outtmpl': os.path.join('./download', f'{title_clean}.%(ext)s'),
            'format': 'best',
            'merge_output_format': 'mp4'
        }
        
        success = multi_round_download(page_url, ydl_opts, auth_opts, max_rounds=3, max_retries=3)
        if success:
            print("\n下载完成！请查看下载文件夹：./download")
        else:
            print("\n下载未完成，请检查网络或重试")
        return

    print("\n检测到以下清晰度可供选择:")
    option_idx = 1
    resolution_options = []
    
    for h in sorted_heights:
        if h in single_map and h in video_map:
            # 提供两个选项: 单文件和分离文件
            print(f"{option_idx}. {h}p (单文件-含音频)")
            resolution_options.append((h, True))  # True表示选择单文件
            option_idx += 1
            
            print(f"{option_idx}. {h}p (分离文件-需要合并音频)")
            resolution_options.append((h, False))  # False表示选择分离文件
            option_idx += 1
        elif h in single_map:
            print(f"{option_idx}. {h}p (单文件-含音频)")
            resolution_options.append((h, True))
            option_idx += 1
        else:
            print(f"{option_idx}. {h}p (需要合并音频)")
            resolution_options.append((h, False))
            option_idx += 1

    while True:
        choice = input("\n请输入要下载的选项编号(如 '1'), 或输入 'q' 放弃: ").strip().lower()
        if choice == 'q':
            print("已放弃操作。")
            return
        
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(resolution_options):
                chosen_height, prefer_single_file = resolution_options[idx]
                break
            else:
                print("无效编号，请重新输入。")
        else:
            print("无效输入，请重新输入。")

    # 4. 根据所选选项，设置下载参数
    chosen_res_str = f"{chosen_height}p"
    
    # 询问是否需要自定义文件名
    custom_filename = input("\n是否需要自定义文件名？(y/n，默认n): ").strip().lower()
    if custom_filename == 'y':
        custom_name = input("请输入自定义文件名: ").strip()
        if custom_name:
            # 使用自定义名称，但仍然添加清晰度
            title_clean = sanitize_filename(custom_name)
    
    out_name = f"{title_clean}_{chosen_res_str}.%(ext)s"
    out_dir = "./download"
    os.makedirs(out_dir, exist_ok=True)

    # 构造 yt-dlp 的下载参数
    ydl_opts = {
        'outtmpl': os.path.join(out_dir, out_name),
        # 改进格式选择策略，将在下面根据情况设置
        'format': None,  # 将在下面根据情况设置
        'merge_output_format': 'mp4',
        'retries': 10,
        'fragment_retries': 10,
        'throttled_rate': '1M',
        'ignoreerrors': True,
        'cookiefile': 'cookies.txt' if os.path.exists('cookies.txt') else None,
        # Make aria2c optional with a fallback
        'downloader': 'aria2c' if os.system('aria2c --version > /dev/null 2>&1') == 0 else None,
        'downloader_args': {
            'http': ['--min-split-size=1M', '--max-connection-per-server=16', '--split=32', '--auto-file-renaming=false'],
            'https': ['--min-split-size=1M', '--max-connection-per-server=16', '--split=32', '--auto-file-renaming=false'],
        } if os.system('aria2c --version > /dev/null 2>&1') == 0 else {},
        # Fix YouTube extractor arguments that might be causing issues
        'extractor_args': {
            'youtube': {
                # Removed problematic client settings
                # 'player_client': ['android_embedded', 'web_mobile'],
                'player_skip': ['configs'],
                'skip': ['translated_subs']  # Don't skip dash and hls as they might be needed
            }
        },
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.93 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Sec-Fetch-Mode': 'navigate',
            'Referer': 'https://www.youtube.com/',
        },
        'compat_opts': {
            'youtube-skip-dash-manifest',
            'no-live-chat'
        },
        'socket_timeout': 300,
        'retry_sleep': 30,
        'proxy': os.environ.get('HTTPS_PROXY') or os.environ.get('HTTP_PROXY') or None,  # Add None fallback
        'force-ipv4': True,
        'nocheckcertificate': True,
        'verbose': True,
        **auth_opts  # 添加认证选项
    }

    # prefer_single_file 已经在选择时确定，无需再次询问
    
    # 根据选择进行相应设置
    if prefer_single_file:
        # 有单文件 (含音频)
        format_id = single_map[chosen_height]
        ydl_opts['format'] = format_id
        print(f"\n已选择{chosen_height}p（单文件），即将开始下载...")
    else:
        # 需要合并音频
        # 先检查是否有对应分辨率的视频流
        if chosen_height in video_map:
            # 选中视频流
            video_format_id = video_map[chosen_height]
            
            # 处理音频流选择
            if not audio_list:
                print("未找到可用音频流，无法合并音频。可能会无声。")
                ydl_opts['format'] = video_format_id
            else:
                # 如果有多个音频流，让用户选择
                if len(audio_list) > 1:
                    print("\n检测到多个音频流可供选择:")
                    for i, (abr, audio_id) in enumerate(audio_list, start=1):
                        print(f"{i}. {abr}kbps (格式ID: {audio_id})")
                    
                    # 用户选择音频流
                    audio_choice = ""
                    while True:
                        audio_choice = input("\n请选择音频质量编号(如 '1')，或直接按回车使用最高音质: ").strip()
                        if not audio_choice:  # 用户直接按回车，使用默认
                            selected_audio_id = audio_list[0][1]  # 使用最高码率
                            print(f"已选择默认最高音质 ({audio_list[0][0]}kbps)")
                            break
                        elif audio_choice.isdigit():
                            idx = int(audio_choice) - 1
                            if 0 <= idx < len(audio_list):
                                selected_audio_id = audio_list[idx][1]
                                print(f"已选择 {audio_list[idx][0]}kbps 音质")
                                break
                            else:
                                print("无效编号，请重新输入。")
                        else:
                            print("无效输入，请重新输入。")
                else:
                    # 只有一个音频流，直接使用
                    selected_audio_id = audio_list[0][1]
                    print(f"\n仅检测到一个音频流 ({audio_list[0][0]}kbps)，将直接使用。")
                
                # 设置下载格式
                ydl_opts['format'] = f"{video_format_id}+{selected_audio_id}"
        else:
            # 没有精确匹配的视频流，使用更加通用的格式表达式
            print(f"\n未找到精确匹配 {chosen_height}p 的视频流，使用自适应格式选择...")
            ydl_opts['format'] = f'bestvideo[height<={chosen_height}][vcodec^=avc1]+bestaudio/best[height<={chosen_height}]'
        
        print(f"\n已选择{chosen_height}p（视频+音频分离），yt-dlp会自动下载并合并。")

    # 5. 进行多轮、多次重试下载
    success = multi_round_download(page_url, ydl_opts, max_rounds=3, max_retries=3)

    if success:
        print("\n下载完成！请查看下载文件夹：", out_dir)
    else:
        print("\n下载未完成，请检查网络连接或尝试其他清晰度")
        # 下载失败，询问是否要换其他分辨率
        while True:
            alt = input("\n下载失败，是否尝试选择其他清晰度继续？(y/n): ").strip().lower()
            if alt == 'y':
                main()  # 重新执行主流程
                break
            elif alt == 'n':
                print("已退出程序。")
                break
            else:
                print("无效输入，请重新输入。")

if __name__ == "__main__":
    main()
