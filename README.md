# Video Audio Extractor & Converter
# 视频音频提取和转换器

A collection of Python scripts for:
- Extracting audio from video files
- Converting between audio formats (MP3, WAV, OGG, M4A, FLAC, AAC)
- Converting between video formats (MP4, AVI, MOV, MKV, FLV, WMV, WebM, M4V)
All with graphical user interface support.

一组Python脚本，用于：
- 从视频文件中提取音频
- 在音频格式之间转换（MP3、WAV、OGG、M4A、FLAC、AAC）
- 在视频格式之间转换（MP4、AVI、MOV、MKV、FLV、WMV、WebM、M4V）
所有功能都支持图形用户界面。

## System Requirements 系统要求

- Python 3.12 or higher (recommended) Python 3.12或更高版本（推荐）
- macOS, Windows, or Linux operating system macOS、Windows或Linux操作系统

## Installation 安装步骤

### 1. Install Python 安装Python

#### macOS:
```bash
# Using Homebrew
brew install python@3.12
brew install python-tk@3.12
```

#### Windows:
- Download Python 3.12 from [python.org](https://www.python.org/downloads/)
- During installation, make sure to check "Add Python to PATH"
- Tkinter is included by default in Windows Python installations

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3.12
sudo apt install python3-tk
```

### 2. Create Virtual Environment 创建虚拟环境

```bash
# Create virtual environment
python3.12 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies 安装依赖

```bash
# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

# Install ffmpeg (required for audio processing)
# macOS:
brew install ffmpeg

# Linux:
sudo apt install ffmpeg

# Windows:
# Download from https://ffmpeg.org/download.html and add to PATH
```

Note: ffmpeg is required for both moviepy and pydub to work properly.
注意：ffmpeg是moviepy和pydub都需要的依赖项。

## Usage 使用方法

1. Activate the virtual environment (if not already activated):
   激活虚拟环境（如果尚未激活）：
   ```bash
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

2. Run either script:
   运行任一脚本：
   ```bash
   # For extracting audio from video:
   # 从视频中提取音频：
   python extract_audio_with_ui.py

   # For converting between audio/video formats:
   # 用于音频/视频格式转换：
   python convert.py
   ```

3. For extract_audio_with_ui.py:
   使用extract_audio_with_ui.py：
   - Use the file dialog to select a video file
   - 使用文件对话框选择视频文件

4. For convert.py:
   使用convert.py：

   The script can be run in two modes:
   脚本可以在两种模式下运行：

   a) Command-line mode (default):
      命令行模式（默认）：
      ```bash
      python convert.py
      ```
      - Choose the type of conversion (1 for audio, 2 for video)
      - 选择转换类型（1表示音频，2表示视频）
      - Select the input file using the file dialog
      - 使用文件对话框选择输入文件
      - Choose the output format by entering the corresponding number:
      - 通过输入对应的数字选择输出格式：
        * For audio 音频格式:
          1. MP3
          2. WAV
          3. OGG
          4. M4A
          5. FLAC
          6. AAC
        * For video 视频格式:
          1. MP4
          2. AVI
          3. MOV
          4. MKV
          5. FLV
          6. WMV
          7. WebM
          8. M4V

   b) GUI mode:
      图形界面模式：
      ```bash
      python convert.py --gui
      ```
      - Select input file through file dialog
      - 通过文件对话框选择输入文件
      - Choose output format from popup menu
      - 从弹出菜单中选择输出格式
      - View conversion result in popup message
      - 在弹出消息中查看转换结果

   Supported formats for convert.py:
   convert.py支持的格式：
   - Input/Output audio formats 音频格式：
     * MP3 (.mp3)
     * WAV (.wav)
     * OGG (.ogg)
     * M4A (.m4a)
     * FLAC (.flac)
     * AAC (.aac)
   
   - Input/Output video formats 视频格式：
     * MP4 (.mp4)
     * AVI (.avi)
     * MOV (.mov)
     * MKV (.mkv)
     * FLV (.flv)
     * WMV (.wmv)
     * WebM (.webm)
     * M4V (.m4v)

5. For audio extraction, choose from the following options:
   从以下选项中选择所需的音频格式：
   - 1: MP3
   - 2: WAV
   - 3: OGG
   - 4: M4A
   - 5: FLAC
   - 6: AAC

6. Wait for the extraction/conversion to complete
   等待提取/转换完成

## Supported Formats 支持的格式

### Audio Formats 音频格式
- MP3 (.mp3)
- WAV (.wav)
- OGG (.ogg)
- M4A (.m4a)
- FLAC (.flac)
- AAC (.aac)

### Video Formats 视频格式
- MP4 (.mp4)
- AVI (.avi)
- MOV (.mov)
- MKV (.mkv)
- FLV (.flv)
- WMV (.wmv)
- WebM (.webm)
- M4V (.m4v)

## Troubleshooting 故障排除

### Tkinter Issues Tkinter问题

If you encounter Tkinter-related errors:
如果遇到Tkinter相关错误：

#### macOS:
```bash
brew install python-tk@3.12
```

#### Linux:
```bash
sudo apt install python3-tk
```

#### Windows:
- Reinstall Python and make sure to check "tcl/tk and IDLE" during installation
  重新安装Python，确保在安装过程中选中"tcl/tk and IDLE"

### MoviePy Issues MoviePy问题

If you encounter MoviePy-related errors:
如果遇到MoviePy相关错误：

1. Make sure you're using the virtual environment
   确保使用虚拟环境
2. Try reinstalling the dependencies:
   尝试重新安装依赖：
   ```bash
   pip uninstall moviepy
   pip install moviepy==1.0.3
   ```

### SSL Certificate Issues SSL证书问题

If you encounter SSL certificate errors during pip install:
如果在pip安装过程中遇到SSL证书错误：

```bash
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```

## Common Issues and Solutions 常见问题和解决方案

1. **Error: No module named '_tkinter'**
   - This means Tkinter is not installed properly
   - Follow the installation steps for your operating system above
   - 这表示Tkinter没有正确安装
   - 按照上述对应操作系统的安装步骤进行安装

2. **Error: No module named 'moviepy.editor'**
   - This usually means the virtual environment is not activated
   - Make sure to activate the virtual environment before running the script
   - 这通常意味着虚拟环境未激活
   - 确保在运行脚本前激活虚拟环境

3. **Error: No module named 'pydub'**
   - This means pydub is not installed properly
   - Make sure to install all requirements: `pip install -r requirements.txt`
   - 这表示pydub没有正确安装
   - 确保安装所有依赖：`pip install -r requirements.txt`

4. **Error: Could not find ffmpeg**
   - MoviePy and pydub both require ffmpeg for audio processing
   - It should be installed automatically with imageio-ffmpeg
   - If issues persist, install ffmpeg manually:
   - MoviePy和pydub都需要ffmpeg进行音频处理
   - 它应该随imageio-ffmpeg自动安装
   - 如果问题持续存在，手动安装ffmpeg：

     ```bash
     # macOS:
     brew install ffmpeg

     # Linux:
     sudo apt install ffmpeg

     # Windows:
     # Download from https://ffmpeg.org/download.html
     ```

5. **Error: Invalid output format**
   - Make sure to enter a valid number for the format selection
   - For audio: enter 1-6 for MP3, WAV, OGG, M4A, FLAC, or AAC
   - For video: enter 1-8 for MP4, AVI, MOV, MKV, FLV, WMV, WebM, or M4V
   - 确保输入有效的格式选择数字
   - 音频格式：输入1-6选择MP3、WAV、OGG、M4A、FLAC或AAC
   - 视频格式：输入1-8选择MP4、AVI、MOV、MKV、FLV、WMV、WebM或M4V

## Notes 注意事项

- Always use a virtual environment to avoid conflicts with system Python packages
  始终使用虚拟环境以避免与系统Python包冲突
- Keep the requirements.txt file in the same directory as the script
  将requirements.txt文件保存在与脚本相同的目录中
- Make sure to have sufficient disk space for audio extraction
  确保有足够的磁盘空间用于音频提取
- Large video files may take longer to process
  大型视频文件可能需要更长的处理时间

## File Structure 文件结构

```
.
├── extract_audio_with_ui.py    # Audio extraction script 音频提取脚本
├── convert.py                  # Format conversion script 格式转换脚本
├── requirements.txt            # Dependencies 依赖项
└── README.md                  # Documentation 文档
