[app]

# (str) Title of your application
title = 错题工具

# (str) Package name
package.name = cuoti_tool

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json,txt,md

# (str) Application versioning (method 1)
version = 2.0.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,pillow,tkinter

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation
# one of landscape, sensorLandscape, portrait or all
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 23b

# (str) Android SDK version to use
android.sdk = 31

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android app theme, default is ok for Kivy-based app
#android.app_theme = "@android:style/Theme.NoTitleBar"

# (list) Pattern to whitelist for the whole project
android.whitelist = 

# (bool) Enable AndroidX support. Enable when 'android.gradle_dependencies'
# contains an 'androidx' package, or any package from Kotlin source.
# android.enable_androidx requires android.api >= 28
android.enable_androidx = True

# (list) add java compile options
# this can for example be necessary when importing certain java libraries using the 'android.gradle_dependencies' option
# see https://developer.android.com/studio/write/java8-support for further information
android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"

# (list) Gradle dependencies to add
android.gradle_dependencies = 

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# In past, was `android.arch` as we weren't supporting builds for multiple archs at the same time.
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) The format used to package the app for release mode (aab or apk).
android.release_artifact = apk

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .aab, .ipa) storage
bin_dir = ./bin

#    -----------------------------------------------------------------------------
#    List as sections
#
#    You can define all the "list" as [section:key].
#    Each line will be considered as a option to the list.
#    Let's take [app] / source.exclude_patterns.
#    Instead of doing:
#
#[app]
#source.exclude_patterns = license,data/audio/*.wav,data/images/original/*
#
#    This can be translated into:
#
#[app:source.exclude_patterns]
#license
#data/audio/*.wav
#data/images/original/*

# (str) Path to a custom kivy-ios folder
#ios.kivy_ios_dir = ../kivy-ios
# Alternately, specify the URL and branch of a git checkout:
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

# Another platform dependency: ios-deploy
# Uncomment to use a custom checkout
#ios.ios_deploy_dir = ../ios_deploy
# Or specify URL and branch
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.7.0

# (str) Name of the certificate to use for signing the debug version
# Get a list of available identities: xcodebuild -list -identities
#ios.codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"

# (str) The development team to use for signing the debug version
#ios.codesign.development_team.debug = <hexstring>

# (str) Name of the certificate to use for signing the release version
#ios.codesign.release = %(ios.codesign.debug)s

# (str) The development team to use for signing the release version
#ios.codesign.development_team.release = <hexstring>

# (str) URL pointing to .ipa file to be installed
# This option should be defined along with `display_image_url` and `full_size_image_url`.
#ios.manifest.app_url = 

# (str) URL pointing to an icon (57x57px) to be displayed during download
# This option should be defined along with `app_url` and `full_size_image_url`.
#ios.manifest.display_image_url = 

# (str) URL pointing to a large icon (512x512px) to be displayed during download
# This option should be defined along with `app_url` and `display_image_url`.
#ios.manifest.full_size_image_url = 

[ios]

# (str) Path to a custom kivy-ios folder
#ios.kivy_ios_dir = ../kivy-ios
# Alternately, specify the URL and branch of a git checkout:
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

# Another platform dependency: ios-deploy
# Uncomment to use a custom checkout
#ios.ios_deploy_dir = ../ios_deploy
# Or specify URL and branch
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.7.0

# (str) URL pointing to .ipa file to be installed
# This option should be defined along with `display_image_url` and `full_size_image_url`.
#ios.manifest.app_url = 

# (str) URL pointing to an icon (57x57px) to be displayed during download
# This option should be defined along with `app_url` and `full_size_image_url`.
#ios.manifest.display_image_url = 

# (str) URL pointing to a large icon (512x512px) to be displayed during download
# This option should be defined along with `app_url` and `display_image_url`.
#ios.manifest.full_size_image_url = 

[android]

# (str) Path to a custom kivy-ios folder
#android.kivy_ios_dir = ../kivy-ios
# Alternately, specify the URL and branch of a git checkout:
android.kivy_ios_url = https://github.com/kivy/kivy-ios
android.kivy_ios_branch = master

# Another platform dependency: ios-deploy
# Uncomment to use a custom checkout
#android.ios_deploy_dir = ../ios_deploy
# Or specify URL and branch
android.ios_deploy_url = https://github.com/phonegap/ios-deploy
android.ios_deploy_branch = 1.7.0

# (str) URL pointing to .ipa file to be installed
# This option should be defined along with `display_image_url` and `full_size_image_url`.
#android.manifest.app_url = 

# (str) URL pointing to an icon (57x57px) to be displayed during download
# This option should be defined along with `app_url` and `full_size_image_url`.
#android.manifest.display_image_url = 

# (str) URL pointing to a large icon (512x512px) to be displayed during download
# This option should be defined along with `app_url` and `display_image_url`.
#android.manifest.full_size_image_url = 

[androidx]

# (bool) Enable AndroidX support. Enable when 'android.gradle_dependencies'
# contains an 'androidx' package, or any package from Kotlin source.
# android.enable_androidx requires android.api >= 28
android.enable_androidx = True

# (list) add java compile options
# this can for example be necessary when importing certain java libraries using the 'android.gradle_dependencies' option
# see https://developer.android.com/studio/write/java8-support for further information
android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"

# (list) Gradle dependencies to add
android.gradle_dependencies = 

[webos]

# (str) URL pointing to .ipa file to be installed
# This option should be defined along with `display_image_url` and `full_size_image_url`.
#webos.manifest.app_url = 

# (str) URL pointing to an icon (57x57px) to be displayed during download
# This option should be defined along with `app_url` and `full_size_image_url`.
#webos.manifest.display_image_url = 

# (str) URL pointing to a large icon (512x512px) to be displayed during download
# This option should be defined along with `app_url` and `display_image_url`.
#webos.manifest.full_size_image_url = 

[windows]

# This section can be used to enable or disable a built-in extension for a specific platform.
# (bool) Enable Windows extension support
windows.enable_ext = False

# (str) Path to a custom kivy-ios folder
#windows.kivy_ios_dir = ../kivy-ios
# Alternately, specify the URL and branch of a git checkout:
windows.kivy_ios_url = https://github.com/kivy/kivy-ios
windows.kivy_ios_branch = master

# Another platform dependency: windows-deploy
# Uncomment to use a custom checkout
#windows.ios_deploy_dir = ../ios_deploy
# Or specify URL and branch
windows.ios_deploy_url = https://github.com/phonegap/ios-deploy
windows.ios_deploy_branch = 1.7.0

# (str) URL pointing to .ipa file to be installed
# This option should be defined along with `display_image_url` and `full_size_image_url`.
#windows.manifest.app_url = 

# (str) URL pointing to an icon (57x57px) to be displayed during download
# This option should be defined along with `app_url` and `full_size_image_url`.
#windows.manifest.display_image_url = 

# (str) URL pointing to a large icon (512x512px) to be displayed during download
# This option should be defined along with `app_url` and `display_image_url`.
#windows.manifest.full_size_image_url = 

[ios]

# (str) Path to a custom kivy-ios folder
#ios.kivy_ios_dir = ../kivy-ios
# Alternately, specify the URL and branch of a git checkout:
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

# Another platform dependency: ios-deploy
# Uncomment to use a custom checkout
#ios.ios_deploy_dir = ../ios_deploy
# Or specify URL and branch
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.7.0

# (str) URL pointing to .ipa file to be installed
# This option should be defined along with `display_image_url` and `full_size_image_url`.
#ios.manifest.app_url = 

# (str) URL pointing to an icon (57x57px) to be displayed during download
# This option should be defined along with `app_url` and `full_size_image_url`.
#ios.manifest.display_image_url = 

# (str) URL pointing to a large icon (512x512px) to be displayed during download
# This option should be defined along with `app_url` and `display_image_url`.
#ios.manifest.full_size_image_url = 

[android]

# (str) Path to a custom kivy-ios folder
#android.kivy_ios_dir = ../kivy-ios
# Alternately, specify the URL and branch of a git checkout:
android.kivy_ios_url = https://github.com/kivy/kivy-ios
android.kivy_ios_branch = master

# Another platform dependency: ios-deploy
# Uncomment to use a custom checkout
#android.ios_deploy_dir = ../ios_deploy
# Or specify URL and branch
android.ios_deploy_url = https://github.com/phonegap/ios-deploy
android.ios_deploy_branch = 1.7.0

# (str) URL pointing to .ipa file to be installed
# This option should be defined along with `display_image_url` and `full_size_image_url`.
#android.manifest.app_url = 

# (str) URL pointing to an icon (57x57px) to be displayed during download
# This option should be defined along with `app_url` and `full_size_image_url`.
#android.manifest.display_image_url = 

# (str) URL pointing to a large icon (512x512px) to be displayed during download
# This option should be defined along with `app_url` and `full_size_image_url`.
#android.manifest.full_size_image_url = 

[androidx]

# (bool) Enable AndroidX support. Enable when 'android.gradle_dependencies'
# contains an 'androidx' package, or any package from Kotlin source.
# android.enable_androidx requires android.api >= 28
android.enable_androidx = True

# (list) add java compile options
# this can for example be necessary when importing certain java libraries using the 'android.gradle_dependencies' option
# see https://developer.android.com/studio/write/java8-support for further information
android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"

# (list) Gradle dependencies to add
android.gradle_dependencies = 

[webos]

# (str) URL pointing to .ipa file to be installed
# This option should be defined along with `display_image_url` and `full_size_image_url`.
#webos.manifest.app_url = 

# (str) URL pointing to an icon (57x57px) to be displayed during download
# This option should be defined along with `app_url` and `full_size_image_url`.
#webos.manifest.display_image_url = 

# (str) URL pointing to a large icon (512x512px) to be displayed during download
# This option should be defined along with `app_url` and `full_size_image_url`.
#webos.manifest.full_size_image_url = 

[windows]

# This section can be used to enable or disable a built-in extension for a specific platform.
# (bool) Enable Windows extension support
windows.enable_ext = False

# (str) Path to a custom kivy-ios folder
#windows.kivy_ios_dir = ../kivy-ios
# Alternately, specify the URL and branch of a git checkout:
windows.kivy_ios_url = https://github.com/kivy/kivy-ios
windows.kivy_ios_branch = master

# Another platform dependency: windows-deploy
# Uncomment to use a custom checkout
#windows.ios_deploy_dir = ../ios_deploy
# Or specify URL and branch
windows.ios_deploy_url = https://github.com/phonegap/ios-deploy
windows.ios_deploy_branch = 1.7.0

# (str) URL pointing to .ipa file to be installed
# This option should be defined along with `display_image_url` and `full_size_image_url`.
#windows.manifest.app_url = 

# (str) URL pointing to an icon (57x57px) to be displayed during download
# This option should be defined along with `app_url` and `full_size_image_url`.
#windows.manifest.display_image_url = 

# (str) URL pointing to a large icon (512x512px) to be displayed during download
# This option should be defined along with `app_url` and `display_image_url`.
#windows.manifest.full_size_image_url = 