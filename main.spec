# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules
from PyInstaller.building.build_main import Tree

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=collect_submodules('Custom_Widgets') + collect_submodules('src'),
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

# Add full folders to the build
a.datas += Tree('Custom_Widgets', prefix='Custom_Widgets')
a.datas += Tree('src', prefix='src')

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='TrustedInApp',  # 👈 Your custom app name here
    icon='assets/images/TRUSTED IN_GREY.png',       # 👈 Add your .ico file here
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,         # 👈 Set to False to remove the terminal window
)
