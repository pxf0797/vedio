# Video Audio Extractor & Converter 🎬⇄🎵

![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)
![Platform](https://img.shields.io/badge/platform-macOS%20|%20Windows%20|%20Linux-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)

A comprehensive toolkit for video/audio processing with GUI support | 支持GUI的视频音频处理工具集

## Table of Contents 📖
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Supported Formats](#supported-formats)
- [Troubleshooting](#troubleshooting)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features ✨
### Core Functionality
- 🎥 Multi-platform video downloading (100+ sources)
- 🔊 High-quality audio extraction from videos
- 🔄 Batch format conversion (audio & video)
- 🖥️ Dual interface mode (CLI & GUI)

### Technical Highlights
- 🚀 Intelligent resolution selection
- 🔁 Automatic retry mechanism (3 attempts)
- 📁 Smart file organization
- 🛠️ FFmpeg backend integration

## Installation 🛠️

### 1. Prerequisites
- Python 3.12+
- FFmpeg (installation instructions below)

### 2. Setup Environment
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

### 3. FFmpeg Installation
| Platform | Command |
|----------|---------|
| **macOS** | `brew install ffmpeg` |
| **Linux** | `sudo apt update && sudo apt install ffmpeg` |
| **Windows** | [Download executable](https://ffmpeg.org/download.html) ➜ Add to PATH |




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


# macOS:
brew install ffmpeg

# Linux:
sudo apt install ffmpeg

# Windows:
# Download from https://ffmpeg.org/download.html and add to PATH
```

Note: ffmpeg is required for video downloading, audio extraction, and format conversion.
注意：ffmpeg是视频下载、音频提取和格式转换所必需的。

## Usage 🚀

### Video Downloader (`video.py`)
```bash
python video.py [--resolution 720p] [--output ./downloads]
```

| Parameter    | Description                          | Default     |
|--------------|--------------------------------------|-------------|
| `--resolution` | Preferred video resolution          | Highest available |
| `--output`     | Output directory path               | ./download  |
| `--retries`    | Maximum download attempts           | 3           |

🖥️ GUI Mode:
```bash
python video.py --gui
```

### Audio Extractor (`extract_audio_with_ui.py`)
```bash
python extract_audio_with_ui.py [input_file] [--format mp3]
```

| Supported Formats | Extensions |
|-------------------|------------|
| MP3               | .mp3       |
| WAV               | .wav       |
| FLAC              | .flac      |
| AAC               | .aac       |

### Format Converter (`convert.py`)
```bash
# Convert video formats
python convert.py input.mp4 --to mov

# Convert audio formats 
python convert.py input.wav --to mp3 --bitrate 320k
```

📊 Quality Options:
```bash
--bitrate    # Audio quality (96k, 128k, 192k, 256k, 320k)
--crf        # Video quality (18-28, lower=better quality)
```

---

### ▶️ Audio Extractor (extract_audio_with_ui.py)
```bash
python extract_audio_with_ui.py
```

**Features**:
- Supports MP3/WAV/OGG/M4A/FLAC/AAC
- Preserves audio quality
- Batch processing support
- Progress visualization

**Usage Steps**:
1. Select video file through GUI
2. Choose output format
3. View conversion progress
4. Get output file in source directory

<!-- zh -->
### ▶️ 音频提取器 (extract_audio_with_ui.py)
```bash
python extract_audio_with_ui.py
```

**功能特性**:
- 支持MP3/WAV/OGG/M4A/FLAC/AAC
- 保持音频质量
- 支持批量处理
- 进度可视化

**使用步骤**:
1. 通过GUI选择视频文件
2. 选择输出格式
3. 查看转换进度
4. 输出文件保存在源目录

---

### ▶️ Format Converter (convert.py)
```bash
python convert.py  # CLI模式
python convert.py --gui  # 图形模式
```

**Conversion Options**:
```bash
# Audio formats:
1. MP3   2. WAV   3. OGG
4. M4A   5. FLAC  6. AAC

# Video formats:
1. MP4   2. AVI   3. MOV   4. MKV
5. FLV   6. WMV   7. WebM  8. M4V
```

<!-- zh -->
### ▶️ 格式转换器 (convert.py)
```bash
python convert.py  # 命令行模式
python convert.py --gui  # 图形界面模式
```

**转换选项**:
```bash
# 音频格式:
1. MP3   2. WAV   3. OGG
4. M4A   5. FLAC  6. AAC

# 视频格式:
1. MP4   2. AVI   3. MOV   4. MKV
5. FLV   6. WMV   7. WebM  8. M4V
```

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

If you encounter "_tkinter" module errors on macOS:

1. Install Tcl/Tk via Homebrew:
```bash
brew install tcl-tk
```

2. Reinstall Python with proper Tcl/Tk support:
```bash
rm -rf ~/.pyenv/versions/3.12.6
export LDFLAGS="-L/opt/homebrew/opt/tcl-tk/lib"
export CPPFLAGS="-I/opt/homebrew/opt/tcl-tk/include"
pyenv install --force 3.12.6 \
  --with-tcltk-includes='-I/opt/homebrew/opt/tcl-tk/include' \
  --with-tcltk-libs='-L/opt/homebrew/opt/tcl-tk/lib -ltcl9.0 -ltk9.0'
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

如果遇到Tkinter相关错误：
1. 通过Homebrew安装Tcl/Tk：
```bash
brew install tcl-tk
```

2. 重新安装Python并启用Tcl/Tk支持：
```bash
rm -rf ~/.pyenv/versions/3.12.6
export LDFLAGS="-L/opt/homebrew/opt/tcl-tk/lib"
export CPPFLAGS="-I/opt/homebrew/opt/tcl-tk/include"
pyenv install --force 3.12.6 \
  --with-tcltk-includes='-I/opt/homebrew/opt/tcl-tk/include' \
  --with-tcltk-libs='-L/opt/homebrew/opt/tcl-tk/lib -ltcl9.0 -ltk9.0'
```

3. 安装项目依赖：
```bash
pip install -r requirements.txt
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

## Project Structure 🌲

```
VedioPy/
├── src/
│   ├── video/                 # Video downloading core logic
│   ├── audio/                 # Audio processing modules
│   └── gui/                   # GUI components
├── scripts/                   # Utility scripts
├── tests/                     # Unit & integration tests
├── docs/                      # Documentation resources
│
├── video.py                   # Main video download entry point
├── extract_audio_with_ui.py   # Audio extraction GUI application
├── convert.py                 # Format conversion CLI/GUI interface
├── requirements.txt           # Python dependencies
├── .gitignore                 # Version control exclusion rules
└── README.md                  # Project documentation
```

## Contributing 🤝

We welcome contributions! Please follow these steps:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 VedioPy

Permission is hereby granted... (truncated for brevity)
```
