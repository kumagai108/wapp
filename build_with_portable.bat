@echo off
chcp 65001 > nul
echo ========================================
echo Portable Python Setup for Building EXE
echo ========================================
echo.
echo This script helps you build EXE without installing Python system-wide.
echo.
echo Steps:
echo   1. Download Python Portable from:
echo      https://www.python.org/ftp/python/3.11.0/python-3.11.0-embed-amd64.zip
echo.
echo   2. Extract to a folder (e.g., C:\python-portable)
echo.
echo   3. Edit this file and set PYTHON_PATH below
echo.
echo   4. Run this script again
echo.
echo ========================================
echo.

REM ====================================
REM TODO: Set your portable Python path here
REM ====================================
set PYTHON_PATH=C:\python-portable\python.exe

REM Check if path is set
if "%PYTHON_PATH%"=="C:\python-portable\python.exe" (
    echo ERROR: Please edit this file and set PYTHON_PATH to your portable Python location
    echo.
    pause
    exit /b 1
)

REM Check if Python exists
if not exist "%PYTHON_PATH%" (
    echo ERROR: Python not found at: %PYTHON_PATH%
    echo.
    pause
    exit /b 1
)

echo Using: %PYTHON_PATH%
"%PYTHON_PATH%" --version
echo.

REM Install pip in portable Python
echo Installing pip...
"%PYTHON_PATH%" -m ensurepip
echo.

REM Install PyInstaller
echo Installing PyInstaller...
"%PYTHON_PATH%" -m pip install pyinstaller
echo.

REM Build EXE
echo Building EXE...
"%PYTHON_PATH%" -m PyInstaller --onefile --windowed --name meisai_converter --icon=NONE meisai_converter_gui.py
echo.

if exist "dist\meisai_converter.exe" (
    echo ========================================
    echo Success!
    echo ========================================
    echo.
    echo Created: dist\meisai_converter.exe
    echo.
) else (
    echo ERROR: Build failed
    echo.
)

pause
