import os
from tkinter import Tk, filedialog
from moviepy.editor import VideoFileClip

def extract_audio_from_video(video_path):
    """
    从视频文件中提取音频并保存为与原文件名相同的音频文件。
    
    :param video_path: 视频文件路径
    """
    try:
        # 验证文件是否存在
        if not os.path.exists(video_path):
            print(f"文件不存在: {video_path}")
            return
            
        # 验证文件大小
        file_size = os.path.getsize(video_path)
        if file_size < 1024:  # 小于1KB的文件可能是损坏的
            print(f"文件可能已损坏或过小: {video_path} ({file_size} bytes)")
            return

        # 获取文件名和目录
        video_dir, video_name = os.path.split(video_path)
        base_name, _ = os.path.splitext(video_name)
        
        # 输出音频文件路径
        output_audio_path = os.path.join(video_dir, f"{base_name}.mp3")
        
        # 加载视频文件
        try:
            video_clip = VideoFileClip(video_path)
        except Exception as e:
            print(f"无法加载视频文件: {e}")
            print("文件可能已损坏或不完整，请尝试重新下载或转换文件格式")
            return
        
        # 提取音频
        audio = video_clip.audio
        if audio is None:
            print("未在视频中找到音频流。")
            return
        
        # 保存音频文件
        audio.write_audiofile(output_audio_path)
        print(f"音频成功提取并保存到: {output_audio_path}")
    
    except Exception as e:
        print(f"提取音频时发生错误: {e}")
    
    finally:
        # 确保释放资源
        if 'audio' in locals() and audio:
            audio.close()
        if 'video_clip' in locals() and video_clip:
            video_clip.close()

def select_video_and_extract_audio():
    """
    打开文件选择对话框，选择视频文件并提取音频。
    """
    # 创建文件选择对话框
    Tk().withdraw()  # 隐藏主窗口
    video_path = filedialog.askopenfilename(
        title="选择视频文件",
        filetypes=[("视频文件", ".mp4 .avi .mov .mkv"), ("所有文件", "*")]
    )
    
    if not video_path:
        print("未选择任何文件。")
        return
    
    print(f"选择的视频文件: {video_path}")
    extract_audio_from_video(video_path)

if __name__ == "__main__":
    select_video_and_extract_audio()
