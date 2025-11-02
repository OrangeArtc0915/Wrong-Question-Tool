@echo off
REM 错题整理工具 - Windows 安装脚本
REM 作者：mmm

echo 错题整理工具 - Windows 安装脚本
echo ==========================

REM 检查Python
echo 检查Python版本...
python --version
if %errorlevel% neq 0 (
    echo 错误：未找到Python，请先安装Python 3.7或更高版本
    echo 下载地址：https://www.python.org/downloads/
    pause
    exit /b 1
)

REM 检查pip
echo 检查pip...
pip --version
if %errorlevel% neq 0 (
    echo 错误：未找到pip，请重新安装Python并确保包含pip
    pause
    exit /b 1
)

REM 询问是否创建虚拟环境
set /p create_venv="是否创建虚拟环境？(y/n): "
if /i "%create_venv%"=="y" (
    echo 创建虚拟环境...
    python -m venv wrong_question_env
    call wrong_question_env\Scripts\activate.bat
    echo 虚拟环境已激活
)

REM 安装依赖
echo 安装Python依赖包...
pip install -r requirements.txt

if %errorlevel% equ 0 (
    echo 依赖安装成功！
) else (
    echo 依赖安装失败，请检查错误信息
    pause
    exit /b 1
)

REM 安装Tesseract OCR
echo.
echo 安装Tesseract OCR...
echo 请下载并安装Tesseract OCR for Windows
echo 下载地址：https://github.com/UB-Mannheim/tesseract/wiki
echo.
echo 安装完成后，请将Tesseract添加到系统PATH环境变量中
echo 或者修改程序中的tesseract_cmd路径

REM 创建程序目录
echo 创建程序目录...
if not exist "CuoTi" mkdir CuoTi

echo.
echo 安装完成！
echo 运行程序：
echo   python wrong_question_tool.py
echo.
echo 作者：mmm
echo 赞助链接：https://gitee.com/orangearc655743/Wrong-Question-Tool.git
pause