# 错题整理工具版本信息
# 作者：mmm

VERSION = "2.0.0"
RELEASE_DATE = "2025-11-02"
AUTHOR = "mmm"
SPONSOR_LINK = "https://gitee.com/orangearc655743/Wrong-Question-Tool.git"

# 版本更新记录
CHANGELOG = """
v2.0.0 (2025-11-02)
- 🐛 修复图片保存BUG
- ✨ 新增图片裁剪功能（支持自定义和预设裁剪）
- ✨ 新增图片旋转功能（90°/180°/270°/自定义角度）
- ✨ 新增标签管理系统（支持自定义标签和显示）
- ✨ 新增批量重命名功能（支持前缀、后缀、编号）
- ✨ 新增文件搜索功能（实时搜索和结果高亮）
- ✨ 新增统计信息显示（总文件数、大小、学科分布）
- 🎨 全面美化界面（主题样式、改进布局、现代化设计）
- ⚡ 添加快捷键支持（Ctrl+I/R/F， F2， Delete等）
- 🔧 改进右键菜单（根据文件类型显示相应操作）
- 📱 优化跨平台兼容性（改进字体和布局适配）
- 🔧 添加自动备份功能（图片处理前自动备份）
- 🔧 改进设置系统（主题、备份、统计选项）

v1.0.0 (2025-11-01)
- 初始版本发布
- 支持图片导入和分类管理
- 集成OCR文字识别功能
- 支持图片预处理
- 支持PDF和Word导出
- 跨平台支持（Windows/Linux/macOS/Android）
- 学科分类管理
- 文件管理器界面
- 重命名、删除、复制、移动功能
- 批量操作支持
- 配置文件支持
- 完整的安装和打包脚本
"""

# 技术栈信息
TECH_STACK = {
    "编程语言": "Python 3.7+",
    "GUI框架": "Tkinter + ttk",
    "图片处理": "PIL (Pillow), OpenCV",
    "OCR引擎": "Tesseract OCR",
    "PDF生成": "ReportLab",
    "Word生成": "python-docx",
    "数据处理": "NumPy",
    "文件管理": "shutil, os",
    "配置管理": "JSON",
    "界面美化": "ttk.Style",
    "打包工具": "PyInstaller"
}

# 支持的操作系统
SUPPORTED_OS = [
    "Windows 7+",
    "macOS 10.12+",
    "Linux (Ubuntu 18.04+)",
    "Android (通过Termux)"
]

# 支持的文件格式
SUPPORTED_FORMATS = {
    "导入格式": [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff"],
    "导出格式": [".pdf", ".docx"],
    "文本格式": [".txt"]
}