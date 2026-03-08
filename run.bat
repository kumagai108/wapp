@echo off
chcp 65001 > nul
echo ========================================
echo Meisai Converter GUI - Quick Start
echo ========================================
echo.

REM Check if uv is installed
uv --version >nul 2>&1
if errorlevel 1 (
    echo uv is not installed. Trying with Python...
    echo.

    REM Fallback to Python
    python --version >nul 2>&1
    if errorlevel 1 (
        echo ERROR: Neither uv nor Python is installed
        echo.
        echo Please install one of the following:
        echo   1. uv: https://github.com/astral-sh/uv
        echo   2. Python: https://www.python.org/
        echo.
        pause
        exit /b 1
    )

    echo Using: Python
    echo Starting application...
    echo.
    python meisai_converter_gui.py
) else (
    REM Use uv (recommended)
    echo Using: uv (faster, no setup needed!)
    echo Starting application...
    echo.
    uv run meisai_converter_gui.py
)

REM Keep window open if there's an error
if errorlevel 1 (
    echo.
    echo ERROR: Failed to start application
    pause
)
