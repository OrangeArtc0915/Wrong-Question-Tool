#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
错题整理工具 - 打包脚本
作者：mmm
支持平台：Windows, Linux, macOS
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

def setup_pyinstaller():
    """安装PyInstaller"""
    print("安装PyInstaller...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

def create_spec_file():
    """创建PyInstaller spec文件"""
    spec_content = '''
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['wrong_question_tool.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('CuoTi', 'CuoTi'),
        ('config.json', '.'),
    ],
    hiddenimports=[
        'PIL',
        'cv2',
        'numpy',
        'pytesseract',
        'reportlab',
        'docx',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='WrongQuestionTool',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico' if os.path.exists('icon.ico') else None,
)
'''
    
    with open('WrongQuestionTool.spec', 'w', encoding='utf-8') as f:
        f.write(spec_content)

def build_executable():
    """构建可执行文件"""
    print("构建可执行文件...")
    
    # 使用spec文件构建
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--clean",
        "--noconfirm",
        "WrongQuestionTool.spec"
    ]
    
    subprocess.check_call(cmd)

def create_portable_package():
    """创建便携版包"""
    print("创建便携版包...")
    
    # 创建发布目录
    release_dir = Path("release")
    if release_dir.exists():
        shutil.rmtree(release_dir)
    release_dir.mkdir()
    
    # 复制可执行文件
    exe_name = "WrongQuestionTool.exe" if sys.platform == "win32" else "WrongQuestionTool"
    exe_path = Path("dist") / exe_name
    
    if exe_path.exists():
        shutil.copy2(exe_path, release_dir / exe_name)
    else:
        print(f"错误：未找到可执行文件 {exe_path}")
        return False
    
    # 复制必要文件
    files_to_copy = [
        "CuoTi",
        "requirements.txt",
        "README.md",
        "install.sh",
        "install.bat",
        "icon.ico"
    ]
    
    for file_name in files_to_copy:
        file_path = Path(file_name)
        if file_path.exists():
            if file_path.is_dir():
                shutil.copytree(file_path, release_dir / file_name)
            else:
                shutil.copy2(file_path, release_dir / file_name)
    
    # 创建启动脚本
    if sys.platform == "win32":
        # Windows批处理文件
        bat_content = f'''@echo off
echo 错题整理工具
echo 作者：mmm
echo 赞助链接：https://gitee.com/orangearc655743/Wrong-Question-Tool.git
echo.
{exe_name}
pause
'''
        with open(release_dir / "启动程序.bat", 'w', encoding='gbk') as f:
            f.write(bat_content)
    else:
        # Linux/macOS shell脚本
        sh_content = f'''#!/bin/bash
echo "错题整理工具"
echo "作者：mmm"
echo "赞助链接：https://gitee.com/orangearc655743/Wrong-Question-Tool.git"
echo ""
./{exe_name}
'''
        with open(release_dir / "启动程序.sh", 'w', encoding='utf-8') as f:
            f.write(sh_content)
        # 设置执行权限
        os.chmod(release_dir / "启动程序.sh", 0o755)
    
    print(f"便携版已创建：{release_dir}")
    return True

def main():
    """主函数"""
    print("错题整理工具 - 打包脚本")
    print("==========================")
    
    # 检查当前目录
    if not Path("wrong_question_tool.py").exists():
        print("错误：请在项目根目录运行此脚本")
        return 1
    
    try:
        # 安装PyInstaller
        setup_pyinstaller()
        
        # 创建spec文件
        create_spec_file()
        
        # 构建可执行文件
        build_executable()
        
        # 创建便携版包
        if create_portable_package():
            print("\n打包完成！")
            print("发布文件位于 'release' 目录中")
            print("\n作者：mmm")
            print("赞助链接：https://gitee.com/orangearc655743/Wrong-Question-Tool.git")
        else:
            print("\n打包失败！")
            return 1
            
    except Exception as e:
        print(f"\n打包过程中出现错误：{e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())