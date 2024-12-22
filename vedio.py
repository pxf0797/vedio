import os
import requests

def download_video(url: str, file_path: str, max_retries: int = 3, max_rounds: int = 10):
    """
    使用requests从指定URL下载视频并保存到本地，含重试逻辑。
    
    :param url: 视频文件的直链URL
    :param file_path: 要保存的本地文件完整路径
    :param max_retries: 每一轮下载中最多重试次数
    :param max_rounds: 最大轮数（若一轮3次都失败则进入下一轮）
    :return: 下载成功返回 True；全部失败返回 False
    """
    print(f"\n准备下载视频：{url}")
    print(f"保存路径：{file_path}")
    
    # 进行多轮下载尝试
    for round_index in range(1, max_rounds + 1):
        print(f"\n----- 第 {round_index} 轮下载，最多 {max_retries} 次重试 -----")
        
        for retry_index in range(1, max_retries + 1):
            print(f"[尝试 {retry_index}/{max_retries}]...")

            try:
                with requests.get(url, stream=True, timeout=15) as response:
                    response.raise_for_status()
                    
                    with open(file_path, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            if chunk:
                                f.write(chunk)

                # 如果下载成功，直接返回 True
                print("下载成功！")
                return True

            except requests.exceptions.RequestException as e:
                print(f"下载出错：{e}")

        # 如果这一轮的所有重试都失败，则询问是否继续下一轮
        if round_index < max_rounds:
            cont = input("本轮全部失败，是否继续下一轮？(y/n) : ").strip().lower()
            if cont != 'y':
                print("已终止下载流程。")
                return False
        else:
            print("已达到最大轮数，仍然全部失败。")
            return False

def main():
    # 1. 提示用户输入链接（示例：可能是一个网页地址，也可能是直接的mp4地址）
    url_input = input("请输入要下载的视频链接: ").strip()
    if not url_input:
        print("未输入链接，程序退出。")
        return

    # ======================================
    # 2. （示例）此处假设已经解析到多清晰度的直链
    #    在真实环境中，你需要调用自己的逻辑来获取不同分辨率的URL。
    # ======================================
    # 为了演示，这里写死一个多清晰度的映射字典
    # 实际项目中，这部分可能来自网页爬虫、接口、JS解析等
    resolution_links = {
        "1080p": "https://example.com/video_1080p.mp4",
        "720p":  "https://example.com/video_720p.mp4",
        "480p":  "https://example.com/video_480p.mp4",
    }

    print("\n已检测到以下清晰度视频可供下载：")
    for idx, res in enumerate(resolution_links, start=1):
        print(f"{idx}. {res}")

    # 3. 让用户选择清晰度
    res_keys = list(resolution_links.keys())
    while True:
        choice = input("\n请输入要下载的清晰度(如 '1' 或 '720p' ), 或输入 'q' 放弃: ").strip().lower()
        if choice == 'q':
            print("已放弃操作。")
            return
        
        # 判断是序号还是直接输入清晰度
        if choice.isdigit():
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(res_keys):
                chosen_res = res_keys[choice_idx]
                break
            else:
                print("无效的编号，请重新输入。")
        else:
            # 如果用户输入的是类似 '720p' 这样的值
            if choice in resolution_links:
                chosen_res = choice
                break
            else:
                print("无效的清晰度选项，请重新输入。")

    # 4. 如果没有创建 ./download 文件夹，则自动创建
    download_dir = "./download"
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    # 5. 下载文件名可自行设置，这里示例统一用 选择的清晰度.mp4
    video_file_name = f"{chosen_res}.mp4"
    file_path = os.path.join(download_dir, video_file_name)
    
    print(f"\n即将下载 [{chosen_res}] 版本。目标文件: {file_path}")

    # 6. 执行下载逻辑（含重试）
    video_url = resolution_links[chosen_res]
    success = download_video(video_url, file_path)
    
    # 7. 如果失败，询问是否要切换其他清晰度或者放弃
    if not success:
        while True:
            choice = input("\n下载失败，是否尝试选择其他清晰度继续？(y/n) : ").strip().lower()
            if choice == 'y':
                main()  # 这里直接再次调用 main()，也可以改为函数化更灵活
                break
            elif choice == 'n':
                print("已退出程序。")
                break
            else:
                print("无效输入，请重新输入。")
    else:
        print("\n下载流程结束，祝您使用愉快。")

if __name__ == "__main__":
    main()
