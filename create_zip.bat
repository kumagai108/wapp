@echo off
chcp 65001 > nul
echo ========================================
echo Create ZIP Package for Distribution
echo ========================================
echo.

REM Check if EXE exists
if not exist "dist\meisai_converter.exe" (
    echo ERROR: dist\meisai_converter.exe not found
    echo Please run build_gui.bat first
    echo.
    pause
    exit /b 1
)

REM Check if 7-Zip is installed
set "SEVENZIP="
if exist "C:\Program Files\7-Zip\7z.exe" set "SEVENZIP=C:\Program Files\7-Zip\7z.exe"
if exist "C:\Program Files (x86)\7-Zip\7z.exe" set "SEVENZIP=C:\Program Files (x86)\7-Zip\7z.exe"

if "%SEVENZIP%"=="" (
    echo 7-Zip not found. Creating ZIP without password protection...
    echo.
    echo For password-protected ZIP, install 7-Zip from:
    echo https://www.7-zip.org/
    echo.

    REM Use PowerShell to create ZIP (Windows 10+)
    powershell -Command "Compress-Archive -Path 'dist\meisai_converter.exe','README.txt','QUICKSTART.txt' -DestinationPath 'meisai_converter_v1.0.zip' -Force"

    if exist "meisai_converter_v1.0.zip" (
        echo ========================================
        echo Success!
        echo ========================================
        echo.
        echo Created: meisai_converter_v1.0.zip
        echo This ZIP file contains:
        echo   - meisai_converter.exe
        echo   - README.txt
        echo   - QUICKSTART.txt
        echo.
        echo Note: This ZIP has NO password protection
        echo.
    ) else (
        echo ERROR: Failed to create ZIP
    )
) else (
    echo Found 7-Zip: %SEVENZIP%
    echo.
    echo Creating password-protected ZIP...
    echo Password: meisai2026
    echo.

    "%SEVENZIP%" a -tzip -p"meisai2026" -mem=AES256 meisai_converter_v1.0_protected.zip "dist\meisai_converter.exe" "README.txt" "QUICKSTART.txt"

    if exist "meisai_converter_v1.0_protected.zip" (
        echo.
        echo ========================================
        echo Success!
        echo ========================================
        echo.
        echo Created: meisai_converter_v1.0_protected.zip
        echo Password: meisai2026
        echo.
        echo This ZIP file contains:
        echo   - meisai_converter.exe
        echo   - README.txt
        echo   - QUICKSTART.txt
        echo.
        echo Encryption: AES-256
        echo.
        echo IMPORTANT: Share the password separately!
        echo.
    ) else (
        echo ERROR: Failed to create ZIP
    )
)

pause
