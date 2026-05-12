@echo off
setlocal

cd /d "%~dp0..\..\.."

echo Installing ImageTools build requirement...
python -m pip install -r AI\ImageTools\Requirements\build.txt
if errorlevel 1 goto fail

echo Building Aetherion ImageTools EXE...
python AI\ImageTools\Build\build_exe.py
if errorlevel 1 goto fail

echo.
echo Build finished.
pause
exit /b 0

:fail
echo.
echo Build failed. Check the messages above.
pause
exit /b 1

