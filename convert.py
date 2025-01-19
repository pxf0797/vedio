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

def convert_video(input_file, output_file):
    try:
        from moviepy.editor import VideoFileClip
        video = VideoFileClip(input_file)
        video.write_videofile(output_file, codec='libx264')
        return f"Success: Video converted to {output_file}"
    except ImportError:
        return "Error: moviepy not installed. Please install it with: pip install moviepy"
    except Exception as e:
        return f"Error converting video: {str(e)}"

def convert_audio(input_file, output_file):
    try:
        audio = AudioSegment.from_file(input_file)
        output_format = os.path.splitext(output_file)[1][1:]  # Get format from extension
        audio.export(output_file, format=output_format)
        return f"Success: Audio converted to {output_file}"
    except Exception as e:
        return f"Error converting audio: {str(e)}"

def get_file_type(file_path):
    if file_path.lower().endswith(('.mp3', '.wav', '.flac')):
        return 'audio'
    elif file_path.lower().endswith(('.mp4', '.mkv', '.avi', '.mov')):
        return 'video'
    return None

def get_output_format(file_type):
    if file_type == 'audio':
        return ['mp3', 'wav', 'flac']
    elif file_type == 'video':
        return ['mp4', 'avi', 'mov']
    return []

def command_line_mode():
    print("请选择要转换的文件格式：")
    print("1. 音频文件 (mp3, wav, flac)")
    print("2. 视频文件 (mp4, avi, mov)")
    choice = input("请输入选项 (1/2): ")
    
    if choice == '1':
        formats = ['mp3', 'wav', 'flac']
    elif choice == '2':
        formats = ['mp4', 'avi', 'mov']
    else:
        print("无效的选择")
        return
    
    input_file = input("请输入输入文件路径: ")
    output_format = input(f"请输入输出格式 ({', '.join(formats)}): ")
    
    if output_format not in formats:
        print(f"无效的输出格式: {output_format}")
        return
    
    output_file = os.path.splitext(input_file)[0] + '.' + output_format
    file_type = get_file_type(input_file)
    
    if file_type == 'audio':
        result = convert_audio(input_file, output_file)
    elif file_type == 'video':
        result = convert_video(input_file, output_file)
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
    
    file_path = filedialog.askopenfilename(title="选择文件")
    if not file_path:
        return
    
    file_type = get_file_type(file_path)
    if not file_type:
        messagebox.showerror("错误", "不支持的文件类型")
        return
    
    formats = get_output_format(file_type)
    format_choice = simpledialog.askstring("选择格式", f"请选择转换格式 ({', '.join(formats)}):")
    
    if not format_choice or format_choice not in formats:
        messagebox.showerror("错误", "无效的格式选择")
        return
    
    output_file = os.path.splitext(file_path)[0] + '.' + format_choice
    
    if file_type == 'audio':
        result = convert_audio(file_path, output_file)
    else:
        result = convert_video(file_path, output_file)
    
    messagebox.showinfo("结果", result)

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
