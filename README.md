# Video Audio Extractor & Converter
# 视频音频提取和转换器

A collection of Python scripts for:
- Downloading videos from various platforms with resolution selection
- Extracting audio from video files
- Converting between audio formats (MP3, WAV, OGG, M4A, FLAC, AAC)
- Converting between video formats (MP4, AVI, MOV, MKV, FLV, WMV, WebM, M4V)
All with user-friendly interfaces.

一组Python脚本，用于：
- 从各种平台下载视频并支持清晰度选择
- 从视频文件中提取音频
- 在音频格式之间转换（MP3、WAV、OGG、M4A、FLAC、AAC）
- 在视频格式之间转换（MP4、AVI、MOV、MKV、FLV、WMV、WebM、M4V）
所有功能都提供友好的用户界面。

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

# Install requirements (includes yt-dlp, moviepy, pydub)
pip install -r requirements.txt

# Install ffmpeg (required for video downloading and processing)
# Video Audio Extractor & Converter
# 视频音频提取和转换器

A collection of Python scripts for:
- Downloading videos with resolution selection
- Extracting audio from video files
- Converting between audio formats (MP3, WAV, OGG, M4A, FLAC, AAC)
- Converting between video formats (MP4, AVI, MOV, MKV, FLV, WMV, WebM, M4V)
All with user-friendly interfaces.

一组Python脚本，用于：
- 下载视频并支持清晰度选择
- 从视频文件中提取音频
- 在音频格式之间转换（MP3、WAV、OGG、M4A、FLAC、AAC）
- 在视频格式之间转换（MP4、AVI、MOV、MKV、FLV、WMV、WebM、M4V）
所有功能都提供友好的用户界面。

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


3. For video.py:
   使用video.py：
   
   Features 功能特点:
   - Downloads videos from various platforms using yt-dlp
   - 使用yt-dlp从各种平台下载视频
   - Automatically detects available resolutions
   - 自动检测可用的视频清晰度
   - Shows resolution options with format details (single file/separate audio)
   - 显示清晰度选项及格式详情（单文件/分离音频）
   - Downloads to './download' folder with sanitized filenames
   - 下载到'./download'文件夹，自动处理文件名
   
   Usage steps 使用步骤:
   a) Enter video URL 输入视频链接
   b) Choose resolution from available options 从可用选项中选择清晰度:
      - Resolutions are sorted high to low 清晰度从高到低排序
      - Shows if audio is included 显示是否包含音频
      - Shows if separate audio download is needed 显示是否需要单独下载音频
   c) Download process 下载过程:
      - Automatic retries (3 rounds, 3 attempts each) 自动重试（3轮，每轮3次）
      - Option to continue next round on failure 失败时可选择继续下一轮
      - Option to try different resolution if all attempts fail 全部失败可选择其他清晰度
   d) Output 输出:
      - Files saved in './download' folder 文件保存在'./download'文件夹
      - Filename includes title and resolution 文件名包含标题和清晰度
      - Automatic audio merging if needed 需要时自动合并音频
# Video Audio Extractor & Converter
# 视频音频提取和转换器

A collection of Python scripts for:
- Downloading videos with resolution selection
- Extracting audio from video files
- Converting between audio formats (MP3, WAV, OGG, M4A, FLAC, AAC)
- Converting between video formats (MP4, AVI, MOV, MKV, FLV, WMV, WebM, M4V)
All with user-friendly interfaces.

一组Python脚本，用于：
- 下载视频并支持清晰度选择
- 从视频文件中提取音频
- 在音频格式之间转换（MP3、WAV、OGG、M4A、FLAC、AAC）
- 在视频格式之间转换（MP4、AVI、MOV、MKV、FLV、WMV、WebM、M4V）
所有功能都提供友好的用户界面。

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

3. For video.py:
   使用video.py：
   
   Features 功能特点:
   - Downloads videos from various platforms using yt-dlp
   - 使用yt-dlp从各种平台下载视频
   - Automatically detects available resolutions
   - 自动检测可用的视频清晰度
   - Shows resolution options with format details (single file/separate audio)
   - 显示清晰度选项及格式详情（单文件/分离音频）
   - Downloads to './download' folder with sanitized filenames
   - 下载到'./download'文件夹，自动处理文件名
   
   Usage steps 使用步骤:
   a) Enter video URL 输入视频链接
   b) Choose resolution from available options 从可用选项中选择清晰度:
      - Resolutions are sorted high to low 清晰度从高到低排序
      - Shows if audio is included 显示是否包含音频
      - Shows if separate audio download is needed 显示是否需要单独下载音频
   c) Download process 下载过程:
      - Automatic retries (3 rounds, 3 attempts each) 自动重试（3轮，每轮3次）
      - Option to continue next round on failure 失败时可选择继续下一轮
      - Option to try different resolution if all attempts fail 全部失败可选择其他清晰度
   d) Output 输出:
      - Files saved in './download' folder 文件保存在'./download'文件夹
      - Filename includes title and resolution 文件名包含标题和清晰度
      - Automatic audio merging if needed 需要时自动合并音频
# macOS:
brew install ffmpeg

# Linux:
sudo apt install ffmpeg

# Windows:
# Download from https://ffmpeg.org/download.html and add to PATH
```

Note: ffmpeg is required for video downloading, audio extraction, and format conversion.
注意：ffmpeg是视频下载、音频提取和格式转换所必需的。

## Usage 使用方法

1. Activate the virtual environment (if not already activated):
   激活虚拟环境（如果尚未激活）：
   ```bash
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

2. Run any of the scripts:
   运行任一脚本：
   ```bash
   # For downloading videos:
   # 下载视频：
   python video.py

   # For extracting audio from video:
   # 从视频中提取音频：
   python extract_audio_with_ui.py

   # For converting between audio/video formats:
   # 用于音频/视频格式转换：
   python convert.py
   ```

3. For video.py:
   使用video.py：
   
   Features 功能特点:
   - Downloads videos from various platforms using yt-dlp
   - 使用yt-dlp从各种平台下载视频
   - Automatically detects available resolutions
   - 自动检测可用的视频清晰度
   - Shows resolution options with format details (single file/separate audio)
   - 显示清晰度选项及格式详情（单文件/分离音频）
   - Downloads to './download' folder with sanitized filenames
   - 下载到'./download'文件夹，自动处理文件名
   
   Usage steps 使用步骤:
   a) Enter video URL 输入视频链接
   b) Choose resolution from available options 从可用选项中选择清晰度:
      - Resolutions are sorted high to low 清晰度从高到低排序
      - Shows if audio is included 显示是否包含音频
      - Shows if separate audio download is needed 显示是否需要单独下载音频
   c) Download process 下载过程:
      - Automatic retries (3 rounds, 3 attempts each) 自动重试（3轮，每轮3次）
      - Option to continue next round on failure 失败时可选择继续下一轮
      - Option to try different resolution if all attempts fail 全部失败可选择其他清晰度
   d) Output 输出:
      - Files saved in './download' folder 文件保存在'./download'文件夹
      - Filename includes title and resolution 文件名包含标题和清晰度
      - Automatic audio merging if needed 需要时自动合并音频

4. For extract_audio_with_ui.py:
   使用extract_audio_with_ui.py：
   - Use the file dialog to select a video file
   - 使用文件对话框选择视频文件
   - Choose from the following audio formats:
   - 从以下音频格式中选择：
     * 1: MP3
     * 2: WAV
     * 3: OGG
     * 4: M4A
     * 5: FLAC
     * 6: AAC

5. For convert.py:
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

5. **Error: Video download failed**
   - Check if the URL is valid and accessible
   - Try selecting a different resolution
   - Use the automatic retry feature (3 rounds available)
   - 检查URL是否有效且可访问
   - 尝试选择其他清晰度
   - 使用自动重试功能（可用3轮）

## Notes 注意事项

- Always use a virtual environment to avoid conflicts with system Python packages
  始终使用虚拟环境以避免与系统Python包冲突
- Keep the requirements.txt file in the same directory as the script
  将requirements.txt文件保存在与脚本相同的目录中
- Make sure to have sufficient disk space for video downloads and processing
  确保有足够的磁盘空间用于视频下载和处理
- Large video files may take longer to process
  大型视频文件可能需要更长的处理时间

## File Structure 文件结构

```
.
├── video.py                    # Video download script 视频下载脚本
├── extract_audio_with_ui.py    # Audio extraction script 音频提取脚本
├── convert.py                  # Format conversion script 格式转换脚本
├── requirements.txt            # Dependencies 依赖项
└── README.md                  # Documentation 文档
