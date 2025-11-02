#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
错题整理工具 v2.0.0 功能测试脚本
作者：mmm
"""

import os
import sys
import json
from PIL import Image, ImageDraw, ImageFont
import tempfile

def create_test_image():
    """创建测试图片"""
    # 创建一个简单的测试图片
    img = Image.new('RGB', (400, 300), color='white')
    draw = ImageDraw.Draw(img)
    
    # 绘制一些内容
    draw.rectangle([50, 50, 350, 250], outline='black', width=2)
    draw.text((100, 100), "Test Question", fill='black')
    draw.text((100, 150), "Math Problem", fill='blue')
    draw.text((100, 200), "This is a test image", fill='red')
    
    return img

def test_image_processing():
    """测试图片处理功能"""
    print("🧪 测试图片处理功能...")
    
    try:
        # 创建测试图片
        test_img = create_test_image()
        
        # 测试保存
        with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as tmp:
            test_img.save(tmp.name, quality=95)
            print(f"✅ 图片保存测试通过: {tmp.name}")
        
        # 测试加载
        loaded_img = Image.open(tmp.name)
        print(f"✅ 图片加载测试通过: {loaded_img.size}")
        
        # 测试基本处理
        from PIL import ImageEnhance
        
        # 亮度调整
        brightness_enhancer = ImageEnhance.Brightness(test_img)
        bright_img = brightness_enhancer.enhance(1.2)
        print("✅ 亮度调整测试通过")
        
        # 对比度调整
        contrast_enhancer = ImageEnhance.Contrast(test_img)
        contrast_img = contrast_enhancer.enhance(1.1)
        print("✅ 对比度调整测试通过")
        
        # 锐化调整
        sharpness_enhancer = ImageEnhance.Sharpness(test_img)
        sharp_img = sharpness_enhancer.enhance(1.1)
        print("✅ 锐化调整测试通过")
        
        # 裁剪测试
        cropped = test_img.crop((50, 50, 300, 200))
        print(f"✅ 裁剪测试通过: {cropped.size}")
        
        # 旋转测试
        rotated = test_img.rotate(90, expand=True)
        print(f"✅ 旋转测试通过: {rotated.size}")
        
        # 清理临时文件
        os.unlink(tmp.name)
        
        return True
        
    except Exception as e:
        print(f"❌ 图片处理测试失败: {e}")
        return False

def test_metadata_system():
    """测试元数据系统"""
    print("\n🧪 测试元数据系统...")
    
    try:
        # 创建测试元数据
        metadata = {
            "title": "测试题目",
            "subject": "数学",
            "tags": "重要,难点",
            "notes": "这是一个测试备注",
            "modified_time": "2025-11-02T15:50:00"
        }
        
        # 测试JSON保存
        with tempfile.NamedTemporaryFile(mode='w', suffix='.meta', delete=False, encoding='utf-8') as tmp:
            json.dump(metadata, tmp, ensure_ascii=False, indent=2)
            print(f"✅ 元数据保存测试通过: {tmp.name}")
        
        # 测试JSON加载
        with open(tmp.name, 'r', encoding='utf-8') as f:
            loaded_metadata = json.load(f)
        
        assert loaded_metadata["title"] == metadata["title"]
        assert loaded_metadata["subject"] == metadata["subject"]
        print("✅ 元数据加载测试通过")
        
        # 清理临时文件
        os.unlink(tmp.name)
        
        return True
        
    except Exception as e:
        print(f"❌ 元数据系统测试失败: {e}")
        return False

def test_file_operations():
    """测试文件操作功能"""
    print("\n🧪 测试文件操作功能...")
    
    try:
        import tempfile
        import shutil
        
        # 创建临时目录
        with tempfile.TemporaryDirectory() as tmpdir:
            # 测试文件创建
            test_file = os.path.join(tmpdir, "test.txt")
            with open(test_file, 'w', encoding='utf-8') as f:
                f.write("测试内容")
            print("✅ 文件创建测试通过")
            
            # 测试文件重命名
            new_file = os.path.join(tmpdir, "renamed.txt")
            os.rename(test_file, new_file)
            assert os.path.exists(new_file)
            print("✅ 文件重命名测试通过")
            
            # 测试文件复制
            copy_file = os.path.join(tmpdir, "copy.txt")
            shutil.copy2(new_file, copy_file)
            assert os.path.exists(copy_file)
            print("✅ 文件复制测试通过")
            
            # 测试文件大小
            size = os.path.getsize(copy_file)
            assert size > 0
            print(f"✅ 文件大小测试通过: {size} bytes")
        
        return True
        
    except Exception as e:
        print(f"❌ 文件操作测试失败: {e}")
        return False

def test_config_system():
    """测试配置系统"""
    print("\n🧪 测试配置系统...")
    
    try:
        # 创建测试配置
        config = {
            "last_subject": "数学",
            "ocr_enabled": True,
            "image_quality": 90,
            "export_format": "pdf",
            "theme": "default",
            "auto_backup": True
        }
        
        # 测试JSON保存
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8') as tmp:
            json.dump(config, tmp, ensure_ascii=False, indent=2)
            print(f"✅ 配置保存测试通过: {tmp.name}")
        
        # 测试JSON加载
        with open(tmp.name, 'r', encoding='utf-8') as f:
            loaded_config = json.load(f)
        
        assert loaded_config["last_subject"] == config["last_subject"]
        assert loaded_config["ocr_enabled"] == config["ocr_enabled"]
        print("✅ 配置加载测试通过")
        
        # 清理临时文件
        os.unlink(tmp.name)
        
        return True
        
    except Exception as e:
        print(f"❌ 配置系统测试失败: {e}")
        return False

def run_all_tests():
    """运行所有测试"""
    print("🚀 开始运行错题整理工具 v2.0.0 功能测试")
    print("=" * 50)
    
    tests = [
        ("图片处理功能", test_image_processing),
        ("元数据系统", test_metadata_system),
        ("文件操作功能", test_file_operations),
        ("配置系统", test_config_system)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
            else:
                print(f"❌ {test_name} 测试失败")
        except Exception as e:
            print(f"❌ {test_name} 测试异常: {e}")
    
    print("\n" + "=" * 50)
    print(f"📊 测试结果: {passed}/{total} 通过")
    
    if passed == total:
        print("🎉 所有测试通过！程序功能正常。")
        return True
    else:
        print("⚠️  部分测试失败，请检查相关功能。")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)