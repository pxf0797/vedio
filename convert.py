import os
import sys
import argparse
from pydub import AudioSegment

# Optional GUI imports
GUI_AVAILABLE = False
try:
    import tkinter as tk
    from tkinter import filedialog, messagebox, simpledialog
    GUI_AVAILABLE = True
except ImportError:
    pass

def convert_video(input_file, output_file, speed=1.0):
    try:
        from moviepy.editor import VideoFileClip
        video = VideoFileClip(input_file)
        if speed != 1.0:
            video = video.fx(video.fx.speedx, speed)
        video.write_videofile(output_file, codec='libx264')
        return f"Success: Video converted to {output_file} (speed: {speed}x)"
    except ImportError:
        return "Error: moviepy not installed. Please install it with: pip install moviepy"
    except Exception as e:
        return f"Error converting video: {str(e)}"

def convert_audio(input_file, output_file, speed=1.0):
    try:
        audio = AudioSegment.from_file(input_file)
        if speed != 1.0:
            audio = audio.speedup(playback_speed=speed)
        output_format = os.path.splitext(output_file)[1][1:]  # Get format from extension
        audio.export(output_file, format=output_format)
        return f"Success: Audio converted to {output_file} (speed: {speed}x)"
    except Exception as e:
        return f"Error converting audio: {str(e)}"

def get_file_type(file_path):
    if file_path.lower().endswith(('.mp3', '.wav', '.flac', '.ogg', '.m4a', '.aac')):
        return 'audio'
    elif file_path.lower().endswith(('.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv', '.webm', '.m4v')):
        return 'video'
    return None

def get_output_format(file_type):
    if file_type == 'audio':
        return ['mp3', 'wav', 'ogg', 'm4a', 'flac', 'aac']
    elif file_type == 'video':
        return ['mp4', 'avi', 'mov', 'mkv', 'flv', 'wmv', 'webm', 'm4v']
    return []

def select_input_file(file_type):
    """打开文件选择对话框并返回选择的文件路径"""
    root = tk.Tk()
    root.withdraw()
    
    if file_type == 'audio':
        filetypes = [("音频文件", "*.mp3 *.wav *.flac *.ogg *.m4a *.aac"), ("所有文件", "*")]
    else:
        filetypes = [("视频文件", "*.mp4 *.mkv *.avi *.mov *.flv *.wmv *.webm *.m4v"), ("所有文件", "*")]
    
    file_path = filedialog.askopenfilename(
        title=f"选择{file_type}文件",
        filetypes=filetypes
    )
    
    if not file_path:
        print("未选择任何文件")
        return None
    
    print(f"选择的文件: {file_path}")
    return file_path

def command_line_mode():
    if not GUI_AVAILABLE:
        print("错误：需要Tkinter支持以使用文件选择对话框")
        print("请安装Tkinter或使用图形界面模式")
        return
    
    # 获取速度参数
    speed = 1.0
    speed_input = input("请输入播放速度 (例如 0.5 表示慢速，1.5 表示快速，默认为1.0): ")
    try:
        speed = float(speed_input) if speed_input else 1.0
        if speed <= 0:
            print("速度必须大于0")
            return
    except ValueError:
        print("无效的速度值，使用默认速度1.0")
        speed = 1.0
    
    print("请选择要转换的文件类型：")
    print("1. 音频文件")
    print("   支持格式: MP3, WAV, OGG, M4A, FLAC, AAC")
    print("2. 视频文件")
    print("   支持格式: MP4, AVI, MOV, MKV, FLV, WMV, WebM, M4V")
    choice = input("请输入选项 (1/2): ")
    
    if choice == '1':
        file_type = 'audio'
        formats = ['mp3', 'wav', 'ogg', 'm4a', 'flac', 'aac']
    elif choice == '2':
        file_type = 'video'
        formats = ['mp4', 'avi', 'mov', 'mkv', 'flv', 'wmv', 'webm', 'm4v']
    else:
        print("无效的选择")
        return
    
    input_file = select_input_file(file_type)
    if not input_file:
        return

    print("请选择输出格式：")
    for i, fmt in enumerate(formats, 1):
        print(f"{i}. {fmt}")
    format_choice = input("请输入数字选择格式: ")
    
    try:
        choice_idx = int(format_choice) - 1
        if choice_idx < 0 or choice_idx >= len(formats):
            print("无效的选择")
            return
        output_format = formats[choice_idx]
    except ValueError:
        print("请输入有效的数字")
        return
    
    # 在文件名中添加速度标记
    base_name = os.path.splitext(input_file)[0]
    if speed != 1.0:
        base_name += f"_{speed}x"
    output_file = base_name + '.' + output_format
    file_type = get_file_type(input_file)
    
    if file_type == 'audio':
        result = convert_audio(input_file, output_file, speed)
    elif file_type == 'video':
        result = convert_video(input_file, output_file, speed)
    else:
        print("不支持的文件类型")
        return
    
    print(result)

def gui_mode():
    if not GUI_AVAILABLE:
        print("GUI模式不可用，请安装Tkinter或使用命令行模式")
        return command_line_mode()
        
    root = tk.Tk()
    root.withdraw()
    
    # 获取速度参数
    speed = simpledialog.askfloat("播放速度", 
                                "请输入播放速度 (例如 0.5 表示慢速，1.5 表示快速)",
                                minvalue=0.1,
                                initialvalue=1.0)
    if speed is None or speed <= 0:
        messagebox.showerror("错误", "无效的速度值")
        return
    
    file_path = filedialog.askopenfilename(title="选择文件")
    if not file_path:
        return
    
    file_type = get_file_type(file_path)
    if not file_type:
        messagebox.showerror("错误", "不支持的文件类型")
        return
    
    formats = get_output_format(file_type)
    format_prompt = "请选择转换格式：\n" + "\n".join([f"{i+1}. {fmt}" for i, fmt in enumerate(formats)])
    format_choice = simpledialog.askinteger("选择格式", format_prompt, minvalue=1, maxvalue=len(formats))
    
    if not format_choice:
        return
    
    if not format_choice or format_choice < 1 or format_choice > len(formats):
        messagebox.showerror("错误", "无效的选择")
        return
    
    output_format = formats[format_choice - 1]
    # 在文件名中添加速度标记
    base_name = os.path.splitext(file_path)[0]
    if speed != 1.0:
        base_name += f"_{speed}x"
    output_file = base_name + '.' + output_format
    
    try:
        if file_type == 'audio':
            result = convert_audio(file_path, output_file, speed)
        else:
            result = convert_video(file_path, output_file, speed)
        messagebox.showinfo("结果", result)
    except Exception as e:
        messagebox.showerror("错误", f"转换失败: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Convert media files between formats")
    parser.add_argument('--gui', action='store_true', help="使用图形界面模式")
    
    args = parser.parse_args()
    
    if args.gui and not GUI_AVAILABLE:
        print("警告：GUI模式不可用，将使用命令行模式")
        print("要启用GUI模式，请确保Tkinter已正确安装")
    
    if args.gui and GUI_AVAILABLE:
        gui_mode()
    else:
        command_line_mode()

if __name__ == "__main__":
    main()
