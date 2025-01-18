import os
from tkinter import Tk, filedialog
from moviepy.editor import VideoFileClip

def extract_audio_from_video(video_path):
    """
    从视频文件中提取音频并保存为与原文件名相同的音频文件。
    
    :param video_path: 视频文件路径
    """
    try:
        # 定义支持的格式和对应的编码器
        supported_formats = {
            '1': {'name': 'MP3', 'codec': 'libmp3lame'},
            '2': {'name': 'WAV', 'codec': 'pcm_s16le'},
            '3': {'name': 'OGG', 'codec': 'libvorbis'},
            '4': {'name': 'M4A', 'codec': 'aac'},
            '5': {'name': 'FLAC', 'codec': 'flac'},
            '6': {'name': 'AAC', 'codec': 'aac'}
        }
        
        # 显示格式选择提示
        print("请选择音频格式:")
        for num, fmt in supported_formats.items():
            print(f"{num}. {fmt['name']}")
        
        # 获取用户选择
        while True:
            try:
                choice = input("请输入数字选择 (默认1): ").strip()
                if not choice:
                    print("将使用默认格式: MP3")
                    format_choice = "mp3"
                    break
                elif choice == "1":
                    format_choice = "mp3"
                    break
                elif choice == "2":
                    format_choice = "wav"
                    break
                elif choice == "3":
                    format_choice = "ogg"
                    break
                elif choice == "4":
                    format_choice = "m4a"
                    break
                elif choice == "5":
                    format_choice = "flac"
                    break
                elif choice == "6":
                    format_choice = "aac"
                    break
                else:
                    print("无效选择，请输入1、2、3、4、5或6")
            except KeyboardInterrupt:
                print("\n操作已取消")
                return
            except Exception as e:
                print(f"输入错误: {e}")
                continue
                
        # 确认选择
        print(f"\n您选择的格式: {format_choice.upper()}")
        confirm = input("是否继续? (y/n): ").strip().lower()
        if confirm != 'y':
            print("操作已取消")
            return

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
        output_audio_path = os.path.join(video_dir, f"{base_name}.{format_choice}")
        
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
        
        # 定义格式对应的编码器
        codec_map = {
            'mp3': 'libmp3lame',
            'wav': 'pcm_s16le',
            'ogg': 'libvorbis',
            'm4a': 'aac',
            'flac': 'flac',
            'aac': 'aac'
        }
        
        # 保存音频文件
        try:
            audio.write_audiofile(output_audio_path, codec=codec_map[format_choice])
            print(f"音频成功提取并保存到: {output_audio_path}")
        except Exception as e:
            print(f"无法保存 {format_choice.upper()} 格式音频: {e}")
            if format_choice != 'mp3':
                print("尝试使用MP3格式...")
                try:
                    output_audio_path = os.path.join(video_dir, f"{base_name}.mp3")
                    audio.write_audiofile(output_audio_path, codec='libmp3lame')
                    print(f"音频已成功保存为MP3格式: {output_audio_path}")
                except Exception as e:
                    print(f"无法保存音频文件: {e}")
                    return
            else:
                print("无法保存音频文件")
                return
    
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
