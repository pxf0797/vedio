# Video Audio Extractor
# 视频音频提取器

A Python script for extracting audio from video files with a graphical user interface.
一个带图形界面的视频音频提取Python脚本。

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
```

## Usage 使用方法

1. Activate the virtual environment (if not already activated):
   激活虚拟环境（如果尚未激活）：
   ```bash
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

2. Run the script:
   运行脚本：
   ```bash
   python extract_audio_with_ui.py
   ```

3. Use the file dialog to select a video file
   使用文件对话框选择视频文件

4. Choose the desired audio format from the following options:
   从以下选项中选择所需的音频格式：
   - 1: MP3
   - 2: WAV
   - 3: OGG
   - 4: M4A
   - 5: FLAC
   - 6: AAC

5. Wait for the extraction to complete
   等待提取完成

## Supported Formats 支持的格式

### Input Video Formats 输入视频格式
- MP4
- AVI
- MOV
- MKV

### Output Audio Formats 输出音频格式
- MP3 (default)
- WAV
- OGG
- M4A
- FLAC
- AAC

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

3. **Error: Could not find ffmpeg**
   - MoviePy requires ffmpeg for audio processing
   - It should be installed automatically with imageio-ffmpeg
   - If issues persist, install ffmpeg manually:
   - MoviePy需要ffmpeg进行音频处理
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
├── extract_audio_with_ui.py    # Main script 主脚本
├── requirements.txt            # Dependencies 依赖项
└── README.md                  # Documentation 文档
