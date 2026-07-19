# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec for the standalone `ntk` executable (Windows + Linux).
import os

block_cipher = None

# All category modules are imported dynamically via importlib -> must be hidden imports.
# v2.0: 33 universal category modules, all lazy-loaded via importlib.
_v2 = [
    'system', 'performance', 'network', 'file', 'text', 'data', 'crypto',
    'security', 'dev', 'git', 'web', 'media', 'docker', 'cloud', 'database',
    'math', 'time', 'convert', 'generate', 'monitor', 'benchmark', 'disk',
    'process', 'search', 'archive', 'image', 'audio', 'code', 'api', 'os',
    'hardware', 'productivity', 'admin',
]
hidden = ['ntk', 'ntk.router', 'ntk.util'] + [f'ntk.v2_{c}' for c in _v2] + [
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
