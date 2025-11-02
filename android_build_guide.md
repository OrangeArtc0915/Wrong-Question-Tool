# Android APK打包指南

## 准备工作

### 1. 安装Java JDK 11+
- 下载并安装Oracle JDK或OpenJDK
- 设置JAVA_HOME环境变量

### 2. 安装Android SDK
- 下载Android Studio
- 安装Android SDK API 31+
- 设置ANDROID_HOME环境变量

### 3. 安装Python打包工具
```bash
pip install buildozer
```

## 打包步骤

### 1. 准备项目文件
确保您的Python项目包含：
- main.py (主程序入口)
- requirements.txt (依赖列表)
- icon.png (应用图标)
- buildozer.spec (配置文件)

### 2. 配置buildozer.spec
```ini
[app]
title = 错题工具
package.name = cuoti_tool
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 2.0.0
requirements = python3,kivy,pillow
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
```

### 3. 执行打包命令
```bash
buildozer android debug
```

### 4. 获取APK文件
APK文件位置: `bin/错题工具-2.0.0-debug.apk`

## 注意事项

1. **首次打包**需要下载大量依赖，可能需要较长时间
2. **网络问题**可能导致下载失败，需要稳定的网络连接
3. **内存要求**打包过程需要至少4GB可用内存
4. **权限设置**根据应用需求添加相应权限

## 常见问题解决

### 1. 编译错误
```bash
# 清理重新编译
buildozer android clean
buildozer android debug
```

### 2. 依赖问题
```bash
# 更新依赖
buildozer android update
```

### 3. 签名发布版本
```bash
buildozer android release
```