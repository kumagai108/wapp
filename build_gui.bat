@echo off
chcp 65001 > nul
echo ========================================
echo Meisai Converter GUI - Build EXE
echo ========================================
echo.

REM Check Python installation
echo [0/4] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)
python --version
echo.

REM Install PyInstaller
echo [1/4] Installing PyInstaller...
echo.

REM Try uv first, fallback to pip
uv --version >nul 2>&1
if errorlevel 1 (
    echo Using: pip
    python -m pip install --upgrade pip
    python -m pip install --upgrade pyinstaller
    if errorlevel 1 (
        echo.
        echo ERROR: Failed to install packages
        echo.
        echo Troubleshooting:
        echo   1. Make sure you have internet connection
        echo   2. Try running as Administrator
        echo   3. Or install uv for easier setup: https://github.com/astral-sh/uv
        echo.
        pause
        exit /b 1
    )
) else (
    echo Using: uv (faster!)
    uv pip install --system pyinstaller
    if errorlevel 1 (
        echo.
        echo ERROR: Failed to install packages
        echo.
        pause
        exit /b 1
    )
)
echo.

REM Clean old build files
echo [3/4] Cleaning old build files...
if exist "dist\meisai_converter.exe" del /q "dist\meisai_converter.exe"
if exist "build" rmdir /s /q "build"
if exist "meisai_converter.spec" del /q "meisai_converter.spec"
echo.

REM Build EXE file
echo [4/4] Building EXE file...
echo This may take a few minutes...
echo.
echo Note: Using --noupx option to reduce false positive virus detection
python -m PyInstaller --onefile --windowed --name meisai_converter --clean --noupx --icon=NONE meisai_converter_gui.py
if errorlevel 1 (
    echo.
    echo ERROR: Failed to build EXE
    echo.
    echo Troubleshooting:
    echo   1. Check if meisai_converter_gui.py exists in this folder
    echo   2. Try: python -m pip uninstall pyinstaller
    echo           python -m pip install pyinstaller
    echo.
    pause
    exit /b 1
)
echo.

echo ========================================
echo Build Complete!
echo ========================================
echo.
echo Created: dist\meisai_converter.exe
echo.
echo Usage:
echo   Double-click dist\meisai_converter.exe to start
echo.
pause
