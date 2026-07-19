@echo off
setlocal
cd /d "D:\software entwicklung\ntk"
echo === Python version ===
python --version
echo === Ensuring psutil present (optional dep) ===
python -m pip install --quiet --disable-pip-version-check psutil 2>nul
echo === Running PyInstaller ===
python -m PyInstaller --clean --noconfirm ntk.spec
echo === Result ===
dir dist
