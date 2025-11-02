# 错题整理工具 - 详细安装指南

## 📋 安装前准备

### 系统要求
- **Windows**: Windows 7 或更高版本（推荐 Windows 10+）
- **macOS**: macOS 10.12 或更高版本（推荐 macOS 12+）
- **Linux**: Ubuntu 18.04+ 或其他主流发行版
- **Python**: 3.7 或更高版本
- **内存**: 至少 2GB RAM（推荐 4GB+）
- **存储**: 至少 500MB 可用空间

### 检查Python版本
打开终端/命令提示符，运行：
```bash
python --version
# 或者
python3 --version
```

如果没有Python或版本过低，请从 [Python官网](https://www.python.org/downloads/) 下载安装。

## 🚀 快速安装

### Windows用户

#### 方法一：使用安装脚本（推荐）
1. 下载所有项目文件到一个文件夹
2. 双击运行 `install.bat`
3. 等待安装完成
4. 双击 `start.bat` 启动程序

#### 方法二：使用环境设置脚本
1. 双击运行 `setup.bat`
2. 按照提示完成Python依赖安装
3. 手动安装Tesseract OCR
4. 运行 `start.bat` 启动程序

### macOS/Linux用户

#### 使用安装脚本
```bash
# 给脚本执行权限
chmod +x install.sh

# 运行安装脚本
./install.sh

# 启动程序
chmod +x start.sh
./start.sh
```

## 📦 详细安装步骤

### 步骤1：安装Python依赖

#### 自动安装（推荐）
```bash
pip install -r requirements.txt
```

#### 手动安装
```bash
pip install pillow>=10.0.0
pip install pytesseract>=0.3.10
pip install reportlab>=4.0.0
pip install python-docx>=0.8.11
pip install opencv-python>=4.8.0
pip install numpy>=1.24.0
```

### 步骤2：安装Tesseract OCR

#### Windows
1. 访问 [Tesseract OCR Windows版本](https://github.com/UB-Mannheim/tesseract/wiki)
2. 下载最新的Windows安装包（通常是 `tesseract-ocr-w64-setup-5.x.x.exe`）
3. 运行安装程序，**重要**：勾选"Add to PATH"选项
4. 安装完成后重启命令提示符

#### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install -y tesseract-ocr tesseract-ocr-chi-sim
```

#### CentOS/RHEL/Fedora
```bash
# CentOS/RHEL
sudo yum install -y tesseract tesseract-langpack-chi-sim

# Fedora
sudo dnf install -y tesseract tesseract-langpack-chi-sim
```

#### macOS
```bash
# 使用Homebrew
brew install tesseract

# 验证安装
tesseract --version
```

### 步骤3：验证安装

运行测试脚本检查环境：
```bash
python test.py
```

如果所有测试通过，说明安装成功。

### 步骤4：启动程序

#### Windows
```cmd
python wrong_question_tool.py
```
或者双击 `start.bat`

#### macOS/Linux
```bash
python3 wrong_question_tool.py
```
或者运行 `./start.sh`

## 🔧 常见安装问题

### 问题1：Python命令不存在
**症状**: `'python' 不是内部或外部命令`

**解决方案**:
1. 确认Python已正确安装
2. 尝试使用 `python3` 替代 `python`
3. 将Python添加到系统PATH环境变量

### 问题2：pip安装失败
**症状**: `pip install` 报错网络错误或权限错误

**解决方案**:
```bash
# 升级pip
python -m pip install --upgrade pip

# 使用国内镜像源
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

# Linux/macOS使用sudo（不推荐）
sudo pip install -r requirements.txt
```

### 问题3：Tesseract OCR未找到
**症状**: `TesseractNotFoundError`

**解决方案**:
1. **Windows**: 确认勾选了"Add to PATH"选项，或手动添加到PATH
2. **Linux**: 安装tesseract包
3. **macOS**: 使用Homebrew安装

### 问题4：缺少tkinter
**症状**: `No module named 'tkinter'`

**解决方案**:
- **Ubuntu/Debian**: `sudo apt-get install python3-tk`
- **CentOS/RHEL**: `sudo yum install tkinter`
- **macOS**: tkinter通常随Python自带
- **Windows**: 重新安装Python，确保包含tkinter

### 问题5：权限不足
**症状**: 权限错误，无法创建文件或目录

**解决方案**:
```bash
# Linux/macOS给脚本执行权限
chmod +x install.sh start.sh

# Windows以管理员身份运行命令提示符
```

### 问题6：依赖版本冲突
**症状**: 安装依赖时版本冲突错误

**解决方案**:
```bash
# 创建虚拟环境
python -m venv wrong_question_env

# 激活虚拟环境
# Windows:
wrong_question_env\Scripts\activate
# macOS/Linux:
source wrong_question_env/bin/activate

# 在虚拟环境中安装依赖
pip install -r requirements.txt
```

## 📱 Android安装（Termux）

### 在Android设备上运行

1. **安装Termux**
   - 从F-Droid或GitHub下载Termux

2. **安装Python和依赖**
   ```bash
   pkg update
   pkg install python
   pkg install tesseract-ocr
   pkg install git
   ```

3. **安装Python包**
   ```bash
   pip install -r requirements.txt
   ```

4. **运行程序**
   ```bash
   python wrong_question_tool.py
   ```

**注意**: Android版本功能可能有限，建议使用桌面版本。

## 🎯 性能优化建议

### 提升OCR识别准确率
1. **图片质量**: 使用高分辨率、清晰的图片
2. **光线**: 确保图片光线充足，无阴影
3. **预处理**: 使用程序内置的图片处理功能
4. **语言包**: 安装完整的中文语言包

### 提升程序运行速度
1. **内存**: 确保有足够的可用内存
2. **存储**: 使用SSD硬盘提升文件读写速度
3. **虚拟内存**: 适当增加虚拟内存大小

## 🔄 卸载指南

### 完全卸载
1. 删除程序文件夹
2. 删除虚拟环境（如果使用了）
3. 卸载Python（如果不再需要）
4. 卸载Tesseract OCR（可选）

### 清理残留文件
```bash
# 清理Python缓存
find . -name "__pycache__" -type d -exec rm -rf {} +
find . -name "*.pyc" -delete

# 清理构建文件
rm -rf build/ dist/ *.spec
```

## 📞 获取帮助

如果遇到安装问题：

1. **查看日志**: 程序运行时的错误信息
2. **运行测试**: `python test.py` 检查环境
3. **检查文档**: 查阅README.md和本安装指南
4. **网络搜索**: 搜索具体的错误信息
5. **社区支持**: 在项目页面提交Issue

---

**作者：mmm**  
**赞助链接：https://gitee.com/orangearc655743/Wrong-Question-Tool.git**