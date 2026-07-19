# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec for the NTK Manager (small local web-UI launcher).
import os

block_cipher = None
ROOT = os.path.dirname(SPECPATH)
icon_path = os.path.join(ROOT, 'assets', 'ntk.ico')

a = Analysis(
    [os.path.join(SPECPATH, 'ntk_manage.py')],
    pathex=[ROOT],
    binaries=[],
    datas=([(os.path.join(SPECPATH, 'catalog.json'), '.')]
           if os.path.exists(os.path.join(SPECPATH, 'catalog.json')) else []),
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=['tkinter', 'test', 'unittest', 'PIL', 'numpy', 'pandas', 'scipy'],
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='ntk-manager',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icon_path if os.path.exists(icon_path) else None,
)
