#!/bin/bash

echo "========================================"
echo "Meisai Converter GUI - Quick Start"
echo "========================================"
echo ""

# Check if uv is installed
if command -v uv &> /dev/null; then
    # Use uv (recommended)
    echo "Using: uv (faster, no setup needed!)"
    echo ""
    echo "Starting application..."
    echo ""
    uv run meisai_converter_gui.py
    exit_code=$?
elif command -v python3 &> /dev/null; then
    # Fallback to Python
    echo "uv is not installed. Using Python instead."
    echo "Using: $(python3 --version)"
    echo ""
    echo "Starting application..."
    echo ""
    python3 meisai_converter_gui.py
    exit_code=$?
else
    echo "ERROR: Neither uv nor Python 3 is installed"
    echo ""
    echo "Please install one of the following:"
    echo "  1. uv: https://github.com/astral-sh/uv"
    echo "  2. Python 3: https://www.python.org/"
    echo ""
    read -p "Press Enter to exit..."
    exit 1
fi

# Check exit status
if [ $exit_code -ne 0 ]; then
    echo ""
    echo "ERROR: Failed to start application"
    read -p "Press Enter to exit..."
fi
