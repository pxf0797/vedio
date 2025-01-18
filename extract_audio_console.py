import os
from moviepy.editor import VideoFileClip

def extract_audio_from_video(video_path):
    """
    从视频文件中提取音频并保存为与原文件名相同的音频文件。
    
    :param video_path: 视频文件路径
    """
    try:
        # 检查视频文件是否存在
        if not os.path.exists(video_path):
            print(f"视频文件不存在: {video_path}")
            return
        
        # 获取文件名和目录
        video_dir, video_name = os.path.split(video_path)
        base_name, _ = os.path.splitext(video_name)
        
        # 输出音频文件路径
        output_audio_path = os.path.join(video_dir, f"{base_name}.mp3")
        
        # 加载视频文件
        video_clip = VideoFileClip(video_path)
        
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

if __name__ == "__main__":
    # 提示用户输入视频文件路径
    video_path = input("请输入视频文件的完整路径: ").strip()
    extract_audio_from_video(video_path)
