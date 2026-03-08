================================================================================
Credit Card Statement to Tax Report CSV Converter (GUI Version)
================================================================================

Overview:
  This tool extracts data from credit card CSV files and converts them
  into a format suitable for tax filing applications.


Requirements:
  METHOD 1 (Quick Start - Recommended):
    Option A: uv (Recommended - fastest and easiest!)
      - Install uv from: https://github.com/astral-sh/uv
      - No other setup needed!

    Option B: Python
      - Python 3.7 or later
      - Install from: https://www.python.org/

    Works on Windows, Mac, and Linux

  METHOD 2 (EXE Build):
    - Windows PC with Python 3.7 or later
    - Internet connection (for downloading PyInstaller)
    - Optional: uv (makes installation faster)

  METHOD 3 (EXE Build without Python/uv):
    - See BUILD_OPTIONS.txt for detailed instructions
    - Use GitHub Actions (recommended) or Python Portable


================================================================================
How to Use
================================================================================

METHOD 1: Quick Start (Recommended - No build required!)
----------------------------------------------------------
If you have Python installed:

Windows:
  1. Double-click "run.bat"
  2. The application will start automatically

Mac/Linux:
  1. Double-click "run.sh" (or run: ./run.sh)
  2. The application will start automatically

Then:
  1. Select the target year (default: current year)
  2. Click "Add Files" button and select your CSV file(s)
  3. Click "Start Conversion" button
  4. Choose where to save the output file
  5. Done!


METHOD 2: Build EXE File (For systems without Python)
----------------------------------------------------------
Windows only:

Step 1: Build the EXE File
  1. Double-click "build_gui.bat"
  2. Wait for the build process to complete (may take a few minutes)
  3. The file "dist\meisai_converter.exe" will be created

Step 2: Run the Application
  1. Double-click "dist\meisai_converter.exe"
  2. The GUI window will open

Step 3: Same as METHOD 1 above


Note: You can add multiple CSV files at once. All data will be merged
      and sorted by date.


================================================================================
Input/Output Format
================================================================================

Input CSV Format:
  - Credit card statement CSV (Shift-JIS encoding)
  - Date format: YYMMDD (e.g., 260115 for 2026/01/15)

Output CSV Format:
  - Columns: Date, Amount, Refund, Description
  - Example:
      Date,Amount,Refund,Description
      2026/1/15,5000,,Store Name
      2026/2/20,12000,,Store Name


================================================================================
Notes
================================================================================

- Input files must be in Shift-JIS encoding
- Output files are saved in UTF-8 with BOM (Excel compatible)
- Only data from the specified year will be extracted
- Multiple files will be merged and sorted by date


================================================================================
Troubleshooting
================================================================================

Q: "Python is not installed or not in PATH" error
A: Install Python from https://www.python.org/ and make sure to check
   "Add Python to PATH" during installation

Q: Characters are garbled
A: Check if your input CSV file is in Shift-JIS encoding

Q: No data is extracted
A: Verify that you selected the correct year

Q: Cannot build EXE file (build_gui.bat fails)
A: 1. Make sure Python is installed on your system
   2. Check internet connection (PyInstaller needs to be downloaded)
   3. Try running as Administrator
   4. Or just use METHOD 1 (Quick Start) - no build needed!


================================================================================
File Structure
================================================================================

meisai_converter_gui.py  - Main program (GUI version)
run.bat                  - Quick start script for Windows
run.sh                   - Quick start script for Mac/Linux
build_gui.bat            - Build script to create EXE file (Windows only)
requirements.txt         - Python package dependencies (for EXE build)
README.txt               - This file


================================================================================
Version 1.0.0
License: MIT
================================================================================
