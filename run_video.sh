#!/bin/bash
# YouTube视频下载器启动脚本
# 自动激活Python虚拟环境并运行下载器

set -e  # 出错时退出

# 获取脚本所在目录
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "========================================"
echo "YouTube视频下载器"
echo "========================================"

# 检查虚拟环境目录
VENV_DIR="$SCRIPT_DIR/video"
if [ ! -d "$VENV_DIR" ]; then
    echo "错误: 虚拟环境目录不存在: $VENV_DIR"
    echo "请先创建虚拟环境或检查目录结构"
    exit 1
fi

# 检查虚拟环境是否有效
if [ ! -f "$VENV_DIR/bin/activate" ]; then
    echo "错误: 虚拟环境目录不完整: $VENV_DIR"
    echo "缺少 activate 脚本"
    exit 1
fi

# 激活虚拟环境
echo "激活Python虚拟环境..."
source "$VENV_DIR/bin/activate"

# 检查Python版本
PYTHON_VERSION=$(python --version 2>&1)
echo "使用Python: $PYTHON_VERSION"

# 检查依赖是否已安装
echo "检查Python依赖..."
if ! python -c "import yt_dlp" 2>/dev/null; then
    echo "警告: yt_dlp 未安装，正在安装依赖..."
    pip install -r requirements.txt
else
    echo "依赖检查通过"
fi

# 检查是否有aria2c（可选）
if command -v aria2c &> /dev/null; then
    echo "检测到 aria2c，将用于加速下载"
else
    echo "未检测到 aria2c，使用内置下载器"
fi

# 判断使用哪个脚本
SCRIPT_TO_RUN="video.py"
if [ $# -gt 0 ]; then
    # 如果有参数，使用命令行版本
    SCRIPT_TO_RUN="video_cli.py"
    echo "使用命令行版本: $SCRIPT_TO_RUN"
else
    echo "使用交互式版本: $SCRIPT_TO_RUN"
    echo "提示: 要使用命令行参数，请添加参数运行，例如:"
    echo "  ./run_video.sh https://youtube.com/watch?v=xxx"
    echo "  ./run_video.sh https://youtube.com/watch?v=xxx --resolution 2"
fi

echo "----------------------------------------"

# 运行脚本
if [ $# -eq 0 ]; then
    # 交互模式
    python "$SCRIPT_TO_RUN"
else
    # 命令行模式
    python "$SCRIPT_TO_RUN" "$@"
fi

# 保持虚拟环境激活状态直到脚本结束
echo "========================================"
echo "下载完成"
echo "虚拟环境已激活，可继续使用Python"
echo "退出脚本或关闭终端后虚拟环境将自动停用"