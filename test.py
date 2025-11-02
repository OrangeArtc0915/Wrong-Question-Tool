#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
错题整理工具 - 测试脚本
作者：mmm
"""

import os
import sys
import importlib.util

def test_python_version():
    """测试Python版本"""
    print("测试Python版本...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print(f"❌ Python版本过低: {version.major}.{version.minor}.{version.micro}")
        print("   需要Python 3.7或更高版本")
        return False
    else:
        print(f"✅ Python版本: {version.major}.{version.minor}.{version.micro}")
        return True

def test_dependencies():
    """测试依赖包"""
    print("\n测试依赖包...")
    
    dependencies = [
        ('tkinter', 'tkinter'),
        ('PIL', 'pillow'),
        ('cv2', 'opencv-python'),
        ('numpy', 'numpy'),
        ('pytesseract', 'pytesseract'),
        ('reportlab', 'reportlab'),
        ('docx', 'python-docx')
    ]
    
    missing = []
    
    for module, package in dependencies:
        try:
            spec = importlib.util.find_spec(module)
            if spec is not None:
                print(f"✅ {package}")
            else:
                print(f"❌ {package}")
                missing.append(package)
        except ImportError:
            print(f"❌ {package}")
            missing.append(package)
    
    if missing:
        print(f"\n缺少依赖包: {', '.join(missing)}")
        print("请运行: pip install -r requirements.txt")
        return False
    else:
        print("\n所有依赖包已安装")
        return True

def test_tesseract():
    """测试Tesseract OCR"""
    print("\n测试Tesseract OCR...")
    
    try:
        import pytesseract
        pytesseract.get_tesseract_version()
        print("✅ Tesseract OCR已安装")
        return True
    except Exception as e:
        print(f"❌ Tesseract OCR未正确安装: {e}")
        print("请安装Tesseract OCR")
        return False

def test_file_structure():
    """测试文件结构"""
    print("\n测试文件结构...")
    
    required_files = [
        'wrong_question_tool.py',
        'requirements.txt',
        'README.md'
    ]
    
    missing_files = []
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file}")
            missing_files.append(file)
    
    if missing_files:
        print(f"\n缺少文件: {', '.join(missing_files)}")
        return False
    else:
        print("\n文件结构完整")
        return True

def test_directories():
    """测试目录结构"""
    print("\n测试目录结构...")
    
    # 创建CuoTi目录
    if not os.path.exists('CuoTi'):
        os.makedirs('CuoTi')
        print("✅ 创建CuoTi目录")
    else:
        print("✅ CuoTi目录已存在")
    
    # 测试目录写入权限
    try:
        test_file = os.path.join('CuoTi', 'test.txt')
        with open(test_file, 'w') as f:
            f.write('test')
        os.remove(test_file)
        print("✅ CuoTi目录可写入")
    except Exception as e:
        print(f"❌ CuoTi目录写入权限不足: {e}")
        return False
    
    return True

def run_basic_test():
    """运行基本功能测试"""
    print("错题整理工具 - 系统测试")
    print("=" * 30)
    
    tests = [
        ("Python版本", test_python_version),
        ("依赖包", test_dependencies),
        ("Tesseract OCR", test_tesseract),
        ("文件结构", test_file_structure),
        ("目录权限", test_directories)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        if test_func():
            passed += 1
    
    print(f"\n测试结果: {passed}/{total} 通过")
    
    if passed == total:
        print("🎉 所有测试通过！程序可以正常运行")
        return True
    else:
        print("⚠️  部分测试失败，请解决上述问题后再运行程序")
        return False

def main():
    """主函数"""
    try:
        if run_basic_test():
            print("\n是否现在启动程序？(y/n)")
            choice = input().lower().strip()
            if choice in ['y', 'yes', '是']:
                print("\n启动程序...")
                os.system('python wrong_question_tool.py' if os.name == 'nt' else 'python3 wrong_question_tool.py')
        else:
            print("\n请先解决测试中发现的问题")
    except KeyboardInterrupt:
        print("\n测试被用户中断")
    except Exception as e:
        print(f"\n测试过程中出现错误: {e}")

if __name__ == "__main__":
    main()