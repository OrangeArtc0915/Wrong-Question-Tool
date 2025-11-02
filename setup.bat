@echo off
REM 错题整理工具 - Windows环境设置脚本
REM 作者：mmm

echo 错题整理工具 - Windows环境设置
echo ================================

echo 检查当前Python环境...
python --version
if %errorlevel% neq 0 (
    echo 错误：未找到Python
    echo 请从 https://www.python.org/downloads/ 下载并安装Python 3.7+
    pause
    exit /b 1
)

echo.
echo 检查pip...
pip --version
if %errorlevel% neq 0 (
    echo 错误：未找到pip
    echo 请重新安装Python并确保包含pip
    pause
    exit /b 1
)

echo.
echo 升级pip...
python -m pip install --upgrade pip

echo.
echo 安装依赖包...
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo 依赖安装失败，尝试逐个安装...
    
    pip install pillow
    pip install pytesseract
    pip install reportlab
    pip install python-docx
    pip install opencv-python
    pip install numpy
    
    if %errorlevel% neq 0 (
        echo.
        echo 某些依赖安装失败，请检查网络连接
        pause
        exit /b 1
    )
)

echo.
echo 创建程序目录...
if not exist "CuoTi" mkdir CuoTi

echo.
echo 环境设置完成！
echo.
echo 接下来请手动安装Tesseract OCR：
echo 1. 下载：https://github.com/UB-Mannheim/tesseract/wiki
echo 2. 安装Tesseract
echo 3. 将Tesseract添加到系统PATH环境变量
echo.
echo 运行程序：python wrong_question_tool.py
echo 或双击 start.bat
echo.
pause