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
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21

[buildozer]
log_level = 2
warn_on_root = 1