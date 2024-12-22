import os
import requests
import yt_dlp

def parse_zhihu_formats(page_url):
    """
    使用 yt-dlp 对知乎视频进行解析，获取可用的下载格式信息。
    只提取扩展名为 mp4 的清晰度链接（若有）。
    返回字典: { '1080p': '直链URL', '720p': '直链URL', ... }
    """
    ydl_opts = {
        'quiet': True,       # 不输出多余信息
        'skip_download': True, # 只解析而不下载
    }
    
    print("\n正在尝试解析知乎视频，请稍候...")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(page_url, download=False)

    # info["formats"] 通常包含多个清晰度
    available_formats = {}
    for f in info.get('formats', []):
        ext = f.get('ext', '')
        height = f.get('height', None)
        # 只挑选 mp4 且有 height 的格式
        if ext.lower() == 'mp4' and height is not None:
            key = f"{height}p"
            # 若同一清晰度出现多次，这里会后写覆盖前写，可根据需要做更细的选择
            available_formats[key] = f["url"]
    
    return available_formats

def download_video(url: str, file_path: str, max_retries: int = 3, max_rounds: int = 10) -> bool:
    """
    使用requests从指定URL下载视频并保存到本地，含多轮重试逻辑。
    :param url: 视频文件的直链URL
    :param file_path: 要保存的本地文件完整路径
    :param max_retries: 每一轮下载中最多重试次数
    :param max_rounds: 最大轮数（若一轮3次都失败则进入下一轮，直到max_rounds)
    :return: 下载成功返回 True；全部失败返回 False
    """
    print(f"\n准备下载视频：{url}")
    print(f"保存路径：{file_path}")
    
    for round_index in range(1, max_rounds + 1):
        print(f"\n----- 第 {round_index} 轮下载，最多 {max_retries} 次重试 -----")
        
        for retry_index in range(1, max_retries + 1):
            print(f"[尝试 {retry_index}/{max_retries}]...")
            try:
                with requests.get(url, stream=True, timeout=15) as response:
                    response.raise_for_status()  # 若返回非200会抛异常
                    
                    with open(file_path, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            if chunk:
                                f.write(chunk)

                print("下载成功！")
                return True

            except requests.exceptions.RequestException as e:
                print(f"下载出错：{e}")

        # 如果这一轮 max_retries 都失败，则询问是否继续下一轮
        if round_index < max_rounds:
            cont = input("本轮全部失败，是否继续下一轮？(y/n) : ").strip().lower()
            if cont != 'y':
                print("已终止下载流程。")
                return False
        else:
            print("已达到最大轮数，仍然全部失败。")
            return False

def main():
    # 1. 让用户输入知乎视频链接
    page_url = input("请输入要下载的知乎视频链接: ").strip()
    if not page_url:
        print("未输入链接，程序退出。")
        return
    
    # 2. 用 yt-dlp 来解析，获取所有可用的 mp4 清晰度链接
    format_dict = parse_zhihu_formats(page_url)
    if not format_dict:
        print("未获取到可用的 mp4 清晰度直链，可能是 M3U8 或 DRM 加密，或无权限。")
        print("可尝试直接使用 yt-dlp 进行下载。")
        return

    # 按清晰度从高到低排序，方便用户选择
    # 例如：keys = ['1080p','720p','480p',...]
    sorted_keys = sorted(format_dict.keys(), key=lambda x: int(x.replace('p','')), reverse=True)

    print("\n已检测到以下清晰度视频可供下载：")
    for idx, res in enumerate(sorted_keys, start=1):
        print(f"{idx}. {res}")

    # 3. 让用户选择清晰度
    while True:
        choice = input("\n请输入要下载的清晰度(如 '1' 或 '720p' ), 或输入 'q' 放弃: ").strip().lower()
        if choice == 'q':
            print("已放弃操作。")
            return
        
        if choice.isdigit():
            # 用户输入序号
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(sorted_keys):
                chosen_res = sorted_keys[choice_idx]
                break
            else:
                print("无效的编号，请重新输入。")
        else:
            # 用户输入的是类似 '720p'
            if choice in format_dict:
                chosen_res = choice
                break
            else:
                print("无效的清晰度选项，请重新输入。")

    # 4. 确定下载保存目录
    download_dir = "./download"
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    # 5. 拼接本地保存路径，比如 720p.mp4
    video_file_name = f"{chosen_res}.mp4"
    file_path = os.path.join(download_dir, video_file_name)

    # 6. 执行下载
    video_url = format_dict[chosen_res]
    success = download_video(video_url, file_path)

    # 7. 若下载失败，询问是否要尝试其他清晰度
    if not success:
        while True:
            alt = input("\n下载失败，是否尝试选择其他清晰度继续？(y/n) : ").strip().lower()
            if alt == 'y':
                main()  # 重新跑一遍
                break
            elif alt == 'n':
                print("已退出程序。")
                break
            else:
                print("无效输入，请重新输入。")
    else:
        print("\n下载完成，祝您使用愉快。")

if __name__ == "__main__":
    main()
