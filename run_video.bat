@echo off
REM YouTube视频下载器启动脚本 (Windows)
REM 自动激活Python虚拟环境并运行下载器

echo ========================================
echo YouTube视频下载器
echo ========================================

REM 获取脚本所在目录
set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%"

REM 检查虚拟环境目录
set VENV_DIR=%SCRIPT_DIR%video
if not exist "%VENV_DIR%" (
    echo 错误: 虚拟环境目录不存在: %VENV_DIR%
    echo 请先创建虚拟环境或检查目录结构
    pause
    exit /b 1
)

REM 检查虚拟环境是否有效
if not exist "%VENV_DIR%\Scripts\activate.bat" (
    echo 错误: 虚拟环境目录不完整: %VENV_DIR%
    echo 缺少 activate.bat 脚本
    pause
    exit /b 1
)

REM 激活虚拟环境
echo 激活Python虚拟环境...
call "%VENV_DIR%\Scripts\activate.bat"

REM 检查Python版本
python --version
if errorlevel 1 (
    echo 错误: Python执行失败
    pause
    exit /b 1
)

REM 检查依赖是否已安装
echo 检查Python依赖...
python -c "import yt_dlp" 2>nul
if errorlevel 1 (
    echo 警告: yt_dlp 未安装，正在安装依赖...
    pip install -r requirements.txt
) else (
    echo 依赖检查通过
)

REM 检查是否有aria2c（可选）
where aria2c >nul 2>&1
if not errorlevel 1 (
    echo 检测到 aria2c，将用于加速下载
) else (
    echo 未检测到 aria2c，使用内置下载器
)

REM 判断使用哪个脚本
set SCRIPT_TO_RUN=video.py
if not "%1"=="" (
    REM 如果有参数，使用命令行版本
    set SCRIPT_TO_RUN=video_cli.py
    echo 使用命令行版本: %SCRIPT_TO_RUN%
) else (
    echo 使用交互式版本: %SCRIPT_TO_RUN%
    echo 提示: 要使用命令行参数，请添加参数运行，例如:
    echo   run_video.bat https://youtube.com/watch?v=xxx
    echo   run_video.bat https://youtube.com/watch?v=xxx --resolution 2
)

echo ----------------------------------------

REM 运行脚本
if "%1"=="" (
    REM 交互模式
    python "%SCRIPT_TO_RUN%"
) else (
    REM 命令行模式
    python "%SCRIPT_TO_RUN%" %*
)

echo ========================================
echo 下载完成
echo 虚拟环境已激活，可继续使用Python
echo 关闭此窗口后虚拟环境将自动停用
pause