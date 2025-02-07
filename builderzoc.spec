from kivy_deps import sdl2, glew
from PyInstaller.utils.hooks import collect_submodules, collect_data_files
from PyInstaller.building.build_main import Analysis, PYZ, EXE, COLLECT
import os

app_name = "MyKivyApp"
script_name = "main.py"  # Change this if your script has a different name

# Analysis phase
block_cipher = None

a = Analysis([
    script_name
],
    pathex=[os.getcwd()],
    binaries=[],
    datas=collect_data_files("kivy") + collect_data_files("kivy_deps") + collect_data_files("kivy_garden"),
    hiddenimports=collect_submodules("kivy") + collect_submodules("kivy_deps") + collect_submodules("kivy_garden"),
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    name=app_name,
    debug=False,
    strip=False,
    upx=True,
    console=True  # Change to False if you want a windowed app
)

coll = COLLECT(exe, a.binaries, a.zipfiles, a.datas, strip=False, upx=True, name=app_name)
