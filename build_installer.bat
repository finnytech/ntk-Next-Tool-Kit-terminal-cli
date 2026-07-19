@echo off
cd /d "D:\software entwicklung\ntk"
echo === Building NTK installer ===
python -m PyInstaller --clean --noconfirm installer\ntk_installer.spec
echo === Result ===
dir dist
