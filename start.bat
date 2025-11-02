@echo off
REM 错题整理工具 - Windows启动脚本
REM 作者：mmm

echo 错题整理工具 v1.0.0
echo ====================
echo 作者：mmm
echo 赞助链接：https://gitee.com/orangearc655743/Wrong-Question-Tool.git
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 错误：未找到Python，请先安装Python 3.7或更高版本
    echo 下载地址：https://www.python.org/downloads/
    pause
    exit /b 1
)

REM 检查依赖是否安装
echo 检查依赖包...
python -c "import tkinter, PIL, cv2, pytesseract, reportlab, docx" >nul 2>&1
if %errorlevel% neq 0 (
    echo 警告：缺少依赖包，正在安装...
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo 依赖安装失败，请检查网络连接或手动安装
        pause
        exit /b 1
    )
)

REM 创建必要目录
if not exist "CuoTi" mkdir CuoTi

echo 启动程序...
echo.

REM 启动主程序
python wrong_question_tool.py

if %errorlevel% neq 0 (
    echo.
    echo 程序运行出错
    pause
)