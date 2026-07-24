[app]
title = حاسبة العمر
package.name = agecalculator
package.domain = org.myapp
source.dir = .

# تمت إضافة ttf لضمان تضمين ملف الخط العربي
source.include_exts = py,png,jpg,kv,atlas,ttf

version = 1.0.0

# تمت إضافة arabic_reshaper و python-bidi
requirements = python3,kivy==2.2.1,pillow,datetime,arabic_reshaper,python-bidi

presplash.filename = %(source.dir)s/icon.png
icon.filename = %(source.dir)s/icon.png

orientation = portrait
fullscreen = 0

android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

android.api = 33
android.minapi = 21

android.archs = arm64-v8a, armeabi-v7a
android.androidx = True

[buildozer]
log_level = 2
warn_on_root = 1
