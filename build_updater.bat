@echo off
cd /d "D:\software entwicklung\ntk"
python -m PyInstaller --clean --noconfirm installer\ntk_updater.spec
dir dist
