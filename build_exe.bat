@echo off
title Build 007 FirstLight Ultrawide Fix Installer

echo Installing PyInstaller...
pip install pyinstaller

echo Building EXE...
pyinstaller --onefile --windowed --name 007FirstLightUltrawideFixSetup src/installer.py

echo.
echo Build complete.
echo Your EXE is here:
echo dist\007FirstLightUltrawideFixSetup.exe

pause
