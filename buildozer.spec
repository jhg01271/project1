[app]

# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.myapp

# (list) Application requirements
requirements = python3,kivy,build,appdirs,toml,cython

# (int) Target Android API
android.api = 35

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (str) NDK version to use
android.ndk = 25b

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1
