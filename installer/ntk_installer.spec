# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec for the NTK installer .exe (Windows, UAC admin, onefile).
import os

block_cipher = None

# Spec is invoked from the project root; SPECPATH is .../installer
ROOT = os.path.dirname(SPECPATH)
# Payload: the already-built ntk.exe (expected at <root>/dist/ntk.exe).
payload = os.path.join(ROOT, 'dist', 'ntk.exe')
icon_path = os.path.join(ROOT, 'assets', 'ntk.ico')

datas = []
if os.path.exists(payload):
    datas.append((payload, '.'))

a = Analysis(
    [os.path.join(SPECPATH, 'ntk_installer.py')],
    pathex=[ROOT],
    binaries=[],
    datas=datas,
    hiddenimports=['winreg'],
    hookspath=[],
    runtime_hooks=[],
    excludes=['tkinter', 'test', 'unittest', 'PIL', 'numpy'],
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
    name='ntk-installer',
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
    uac_admin=True,
    icon=icon_path if os.path.exists(icon_path) else None,
)
