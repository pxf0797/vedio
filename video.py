"""
YouTube视频下载工具 - 增强版
支持YouTube视频签名提取失败情况的处理
提供更灵活的格式选择和错误处理

使用方法:
1. 运行脚本: python video.py
2. 输入YouTube视频链接
3. 选择清晰度或格式
4. 
更新日志:
- 增加了对YouTube签名提取失败的处理
- 添加了格式列表显示功能
- 支持自定义格式ID输入
- 改进了错误处理和用户提示
- 优化了下载参数配置
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
    print('setupt cookies example: python -m yt_dlp --cookies-from-browser chrome --verbose --ignore-config "https://www.youtube.com/watch?v=P99ZHIUKAJY&t=3839s"')
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

def parse_formats(page_url: str):
    """
    使用 yt-dlp 提取视频信息，包括标题和所有可用格式。
    返回:
      title (str): 视频标题（若无则空字符串）
      formats (list): 所有可用的格式信息，每个元素是一个 dict
    """
    # 只解析、不下载
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'cookiefile': 'cookies.txt'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(page_url, download=False)
    title = info.get("title") or ""
    formats = info.get("formats", [])
    return title, formats

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

def multi_round_download(page_url, ydl_opts, max_rounds=3, max_retries=3):
    """
    以多轮、每轮多次重试的方式调用 yt-dlp 下载。
    - max_rounds: 最多轮数
    - max_retries: 每轮尝试次数 (在 yt-dlp 里一般只有一次下载机会，出错就需要下一轮)
    
    当出现下载错误时，允许用户输入 y/n 决定是否继续下一轮。
    """
    for round_idx in range(1, max_rounds + 1):
        for retry_idx in range(1, max_retries + 1):
            print(f"\n----- 第 {round_idx} 轮, 第 {retry_idx} 次尝试下载 -----")
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([page_url])
                return True
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
                print(f"下载出错: {e}")
            except Exception as e:
                print(f"下载出错: {e}")

        if round_idx < max_rounds:
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
    title_raw, formats = parse_formats(page_url)
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
            'merge_output_format': 'mp4'
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
        
        success = multi_round_download(page_url, ydl_opts, max_rounds=3, max_retries=3)
        if success:
            print("\n下载完成！请查看下载文件夹：./download")
        else:
            print("\n下载未完成，请检查网络或重试")
        return

    print("\n检测到以下清晰度可供选择:")
    for i, h in enumerate(sorted_heights, start=1):
        print(f"{i}. {h}p", end='')
        if h in single_map and h in video_map:
            print(" (可单文件/可分离)")
        elif h in single_map:
            print(" (单文件-含音频)")
        else:
            print(" (需要合并音频)")

    while True:
        choice = input("\n请输入要下载的清晰度编号(如 '1'), 或输入 'q' 放弃: ").strip().lower()
        if choice == 'q':
            print("已放弃操作。")
            return
        
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(sorted_heights):
                chosen_height = sorted_heights[idx]
                break
            else:
                print("无效编号，请重新输入。")
        else:
            print("无效输入，请重新输入。")

    # 4. 根据所选分辨率，判断是否有单文件
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
        'format': f'bestvideo[height={chosen_height}][vcodec^=avc1]+bestaudio/best[height={chosen_height}]',
        'merge_output_format': 'mp4',
        'retries': 10,
        'fragment_retries': 10,
        'throttled_rate': '1M',
        'ignoreerrors': True,
        'cookiefile': 'cookies.txt' if os.path.exists('cookies.txt') else None,
        'downloader': 'aria2c',
        'downloader_args': {
            'http': ['--min-split-size=1M', '--max-connection-per-server=16', '--split=32', '--auto-file-renaming=false'],
            'https': ['--min-split-size=1M', '--max-connection-per-server=16', '--split=32', '--auto-file-renaming=false'],
        },
        'extractor_args': {
            'youtube': {
                'player_client': ['android_embedded', 'web_mobile'],
                'player_skip': ['configs'],
                'skip': ['hls', 'dash', 'translated_subs']
            }
        },
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.93 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'https://www.youtube.com/',
        },
        'compat_opts': {
            'youtube-skip-dash-manifest',
            'no-live-chat'
        },
        'socket_timeout': 300,
        'retry_sleep': 30,
        'proxy': os.environ.get('HTTPS_PROXY') or os.environ.get('HTTP_PROXY'),
        'force-ipv4': True,
        'nocheckcertificate': True,
        'verbose': True
    }

    if chosen_height in single_map:
        # 有单文件 (含音频)
        format_id = single_map[chosen_height]
        ydl_opts['format'] = format_id
        print(f"\n已选择{chosen_height}p（单文件），即将开始下载并自动合并(若需要)...")
    else:
        # 需要合并音频
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
