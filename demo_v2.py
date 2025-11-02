#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
错题整理工具 v2.0.0 快速演示脚本
作者：mmm
"""

import os
import json
from PIL import Image, ImageDraw, ImageFont
import tempfile

def create_demo_image(filename, content_text):
    """创建演示图片"""
    # 创建一个400x300的白色图片
    img = Image.new('RGB', (400, 300), color='white')
    draw = ImageDraw.Draw(img)
    
    # 绘制边框
    draw.rectangle([20, 20, 380, 280], outline='black', width=3)
    
    # 绘制内容
    draw.text((40, 60), filename, fill='black')
    draw.text((40, 100), content_text, fill='blue')
    draw.text((40, 140), "这是一个演示题目", fill='red')
    draw.text((40, 180), "数学 - 二次函数", fill='green')
    draw.text((40, 220), "难度：中等", fill='purple')
    
    return img

def create_demo_data():
    """创建演示数据"""
    print("🎯 创建错题整理工具 v2.0.0 演示数据...")
    
    # 创建演示目录结构
    demo_dir = "CuoTi_Demo"
    subjects = ["数学", "英语", "物理"]
    
    # 创建学科目录
    for subject in subjects:
        subject_dir = os.path.join(demo_dir, subject)
        os.makedirs(subject_dir, exist_ok=True)
        
        # 为每个学科创建演示图片
        for i in range(1, 4):
            filename = f"{subject}_题目_{i:03d}.jpg"
            content = f"{subject} 演示题目 {i}"
            
            # 创建图片
            img = create_demo_image(filename, content)
            img_path = os.path.join(subject_dir, filename)
            img.save(img_path, quality=95)
            
            # 创建元数据文件
            metadata = {
                "title": f"{subject}题目{i}",
                "subject": subject,
                "tags": f"重要,基础题目,题目{i}",
                "notes": f"这是{subject}学科的第{i}个演示题目，包含基础知识点。",
                "modified_time": "2025-11-02T15:50:00"
            }
            
            meta_filename = f"{subject}_题目_{i:03d}.meta"
            meta_path = os.path.join(subject_dir, meta_filename)
            
            with open(meta_path, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, ensure_ascii=False, indent=2)
            
            print(f"✅ 创建演示文件: {filename}")
    
    print(f"\n🎉 演示数据创建完成！")
    print(f"📁 演示目录: {demo_dir}")
    print(f"📊 包含 {len(subjects)} 个学科，每个学科 3 个演示题目")
    print(f"🏷️  每个题目都包含标签和备注信息")
    
    return demo_dir

def show_feature_demo():
    """展示新功能演示"""
    print("\n" + "="*60)
    print("🎯 错题整理工具 v2.0.0 新功能演示")
    print("="*60)
    
    features = [
        {
            "name": "图片裁剪功能",
            "description": "支持自定义裁剪区域，提供正方形、顶部、中心等预设选项",
            "usage": "工具菜单 → 图片裁剪 或 右键菜单 → 图片裁剪"
        },
        {
            "name": "图片旋转功能", 
            "description": "支持90°/180°/270°旋转和自定义角度旋转",
            "usage": "工具菜单 → 图片旋转 或 右键菜单 → 图片旋转"
        },
        {
            "name": "标签管理系统",
            "description": "为文件添加自定义标签，支持多标签和标签搜索",
            "usage": "编辑菜单 → 添加标签 或 右键菜单 → 添加标签"
        },
        {
            "name": "批量重命名功能",
            "description": "支持设置前缀、后缀、自动编号，实时预览效果",
            "usage": "文件菜单 → 批量重命名"
        },
        {
            "name": "文件搜索功能",
            "description": "实时文件名搜索，搜索结果高亮显示",
            "usage": "工具菜单 → 搜索文件 或 Ctrl+F"
        },
        {
            "name": "统计信息显示",
            "description": "显示总文件数、总大小、按学科分类统计",
            "usage": "视图菜单 → 显示统计信息"
        },
        {
            "name": "快捷键支持",
            "description": "Ctrl+I导入、Ctrl+R刷新、Ctrl+F搜索、F2重命名等",
            "usage": "查看 → 快捷键"
        },
        {
            "name": "界面美化",
            "description": "现代化设计、改进的工具栏、增强的文件列表",
            "usage": "启动程序即可体验"
        }
    ]
    
    for i, feature in enumerate(features, 1):
        print(f"\n{i}. ✨ {feature['name']}")
        print(f"   📝 {feature['description']}")
        print(f"   🎮 使用方法: {feature['usage']}")
    
    print("\n" + "="*60)
    print("🎯 快速开始指南")
    print("="*60)
    
    steps = [
        "1. 运行程序: python wrong_question_tool.py",
        "2. 点击'导入错题'选择图片文件",
        "3. 选择学科进行分类",
        "4. 使用图片处理功能优化图片",
        "5. 添加标签和备注信息",
        "6. 使用搜索功能快速找到文件",
        "7. 导出为PDF或Word格式"
    ]
    
    for step in steps:
        print(f"   {step}")
    
    print("\n" + "="*60)
    print("🚀 现在就开始体验新功能吧！")
    print("="*60)

def main():
    """主函数"""
    print("🎯 错题整理工具 v2.0.0 演示程序")
    print("作者：mmm")
    print("="*50)
    
    # 创建演示数据
    demo_dir = create_demo_data()
    
    # 显示功能演示
    show_feature_demo()
    
    print(f"\n💡 提示：演示数据已创建在 '{demo_dir}' 目录中")
    print("你可以将这些文件复制到程序的CuoTi目录中进行测试")
    
    print("\n🎉 演示完成！感谢体验错题整理工具 v2.0.0")

if __name__ == "__main__":
    main()