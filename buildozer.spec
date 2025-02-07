[app]
title = MyKivyApp
package.name = mykivyapp
package.domain = org.nemaleshwar
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3, kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[android]
package = org.nemaleshwar.mykivyapp
android.api = 30
android.minapi = 21
android.ndk = 23b
