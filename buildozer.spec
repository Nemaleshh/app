[app]
# (str) Title of your application
title = MyKivyApp

# (str) Package name (should be unique)
package.name = mykivyapp

# (str) Package domain (e.g., com.example)
package.domain = org.nemaleshwar

# (str) Source code directory (current directory)
source.dir = .

# (str) The entry point file of your app
source.include_exts = py,png,jpg,kv,atlas
main.py = app.py

# (str) Application version
version = 1.0

# (list) Application requirements (Ensure these match `requirements.txt`)
requirements = python3, kivy

# (bool) Whether to include a custom icon (if you have an icon)
icon.filename = icon.png

# (bool) Whether the application should run in fullscreen
fullscreen = 0

# (str) Application orientation (portrait, landscape, etc.)
orientation = portrait

# (str) Presplash image path (if you have one)
presplash.filename = presplash.png

# (bool) Enable android permissions automatically
android.permissions = INTERNET, ACCESS_NETWORK_STATE

[buildozer]
# (int) Verbosity level (0 to 2)
log_level = 2

# (bool) Whether to allow Buildozer to update itself
warn_on_root = 1

[android]
# (str) Android package name
package = org.nemaleshwar.mykivyapp

# (int) Android API level (target)
android.api = 30

# (int) Minimum API level
android.minapi = 21

# (str) Android NDK version
android.ndk = 23b

# (bool) Enable Android debug mode
android.debug = True

# (list) Additional Android permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (bool) Enable AndroidX support
android.enable_androidx = True

# (bool) Allow running the app in the background
android.service = True

# (list) Additional Java classes (if needed)
android.add_src =
