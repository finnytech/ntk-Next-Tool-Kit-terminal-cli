# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec for the standalone `ntk` executable (Windows + Linux).
import os

block_cipher = None

# All category modules are imported dynamically via importlib -> must be hidden imports.
hidden = [
    'ntk', 'ntk.router', 'ntk.util',
    'ntk.cmd_sys', 'ntk.cmd_net', 'ntk.cmd_file', 'ntk.cmd_text',
    'ntk.cmd_crypto', 'ntk.cmd_dev', 'ntk.cmd_auto', 'ntk.cmd_docker',
    'ntk.cmd_db', 'ntk.cmd_web', 'ntk.cmd_media', 'ntk.cmd_ai',
    'ntk.cmd_sec', 'ntk.cmd_cloud', 'ntk.cmd_util',
    # common optional deps that may be present
    'psutil',
]

icon_path = os.path.join('assets', 'ntk.ico')

a = Analysis(
    ['ntk_main.py'],
    pathex=[os.getcwd()],
    binaries=[],
    datas=[],
    hiddenimports=hidden,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['tkinter', 'test', 'unittest'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
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
    name='ntk',
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
    version='version_info.txt' if os.path.exists('version_info.txt') else None,
)
