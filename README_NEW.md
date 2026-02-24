# YouTube视频下载器 - 增强版使用说明

基于原有的 `video.py` 脚本，新增了命令行版本和启动脚本，简化使用流程。

## 🚀 快速开始

### macOS/Linux
```bash
# 1. 赋予启动脚本执行权限（首次使用）
chmod +x run_video.sh

# 2. 运行交互式版本（推荐新手）
./run_video.sh

# 3. 或者直接下载视频（命令行版本）
./run_video.sh https://youtube.com/watch?v=xxx
```

### Windows
```bash
# 直接运行批处理脚本
run_video.bat

# 或者直接下载视频
run_video.bat https://youtube.com/watch?v=xxx
```

## 📋 新功能特性

### 1. 启动脚本 (`run_video.sh` / `run_video.bat`)
- 自动激活Python虚拟环境（使用 `video/` 目录）
- 自动检查并安装依赖
- 智能选择交互式或命令行模式
- 跨平台支持（macOS/Linux/Windows）

### 2. 命令行版本 (`video_cli.py`)
- 支持命令行参数，无需交互输入
- 批量下载支持
- 灵活的格式选择
- 配置文件支持

### 3. 配置文件 (`config.yaml`)
- 存储用户偏好设置
- 支持默认下载目录、认证方式等
- 命令行参数优先级高于配置文件

## 🎯 使用示例

### 基础用法
```bash
# 交互式选择清晰度和音频（传统方式）
./run_video.sh

# 命令行版本 - 交互式选择
./run_video.sh https://youtube.com/watch?v=xxx

# 命令行版本 - 指定分辨率选项
./run_video.sh https://youtube.com/watch?v=xxx --resolution 2

# 命令行版本 - 指定分辨率和音频
./run_video.sh https://youtube.com/watch?v=xxx --resolution 2 --audio 1
```

### 高级用法
```bash
# 仅列出可用格式，不下载
./run_video.sh https://youtube.com/watch?v=xxx --list

# 指定输出目录
./run_video.sh https://youtube.com/watch?v=xxx --output ./my_videos

# 跳过认证（可能无法下载某些视频）
./run_video.sh https://youtube.com/watch?v=xxx --no-auth

# 使用指定cookie文件
./run_video.sh https://youtube.com/watch?v=xxx --cookies ~/cookies.txt

# 批量下载
./run_video.sh --batch urls.txt
```

### 配置文件示例
编辑 `config.yaml` 文件：
```yaml
defaults:
  download_dir: ./downloads  # 默认下载目录
  format: mp4                # 输出格式

authentication:
  cookies_file: ~/.youtube_cookies.txt  # 默认cookie文件
  browser: chrome                       # 默认浏览器类型

quality:
  preferred_resolution: 1080  # 首选分辨率
  audio_quality: best         # 音频质量
```

## 🔧 命令行参数详解

```
usage: video_cli.py [-h] [-l] [-r RESOLUTION] [-a AUDIO] [-o OUTPUT] [-n NAME]
                    [--no-auth] [--cookies COOKIES] [--browser BROWSER]
                    [--batch BATCH]
                    [url]

YouTube视频下载器 - 命令行版本

positional arguments:
  url                   YouTube视频URL

optional arguments:
  -h, --help            显示帮助信息
  -l, --list            仅列出可用格式，不下载
  -r, --resolution      分辨率选项编号（从1开始）
  -a, --audio           音频选项编号（从1开始）
  -o, --output          输出目录（默认: ./download）
  -n, --name            自定义文件名（不含扩展名）
  --no-auth             跳过认证
  --cookies             指定cookie文件路径
  --browser             指定浏览器类型（用于提取cookies）
  --batch               批量下载URL文件（每行一个URL）
```

## 📁 文件结构

```
Video/
├── video.py              # 原始交互式脚本
├── video_cli.py          # 新命令行版本
├── run_video.sh          # macOS/Linux启动脚本
├── run_video.bat         # Windows启动脚本
├── config.yaml           # 配置文件（可选）
├── requirements.txt      # Python依赖
├── download/             # 下载目录
├── video/                # Python虚拟环境
└── README.md            # 原始说明文档
```

## ⚙️ 虚拟环境说明

项目使用 `video/` 目录作为Python虚拟环境，启动脚本会自动激活。

如需手动使用虚拟环境：
```bash
# macOS/Linux
source video/bin/activate

# Windows
video\Scripts\activate.bat
```

## 🔍 故障排除

### 1. 启动脚本权限问题（macOS/Linux）
```bash
chmod +x run_video.sh
```

### 2. 虚拟环境问题
如果虚拟环境损坏，可重新创建：
```bash
cd /Users/xfpan/Desktop/VedioPy/Video
python -m venv video
source video/bin/activate
pip install -r requirements.txt
```

### 3. 缺少依赖
启动脚本会自动安装依赖，如需手动安装：
```bash
source video/bin/activate
pip install -r requirements.txt
```

### 4. YouTube认证问题
- 使用 `--cookies` 参数指定cookie文件
- 或使用浏览器提取cookies（脚本会引导）
- 或创建 `cookies.txt` 文件在当前目录

## 📞 获取帮助

```bash
# 显示帮助信息
./run_video.sh --help

# 或直接运行Python脚本
source video/bin/activate
python video_cli.py --help
```

## 🔄 与原版的兼容性

- `video.py`: 完全保留，交互式使用
- `video_cli.py`: 新增，命令行使用
- 两者共享相同的下载核心逻辑
- 可单独使用任一版本