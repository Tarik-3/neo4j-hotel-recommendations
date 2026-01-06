@echo off
echo ========================================
echo Hotel Finder - Quick Launch
echo ========================================
echo.

set PYTHON_EXE=C:\Users\tarik\AppData\Local\Programs\Python\Python313\python.exe

echo [1/2] Starting API Server...
start "Hotel API Server" cmd /k "cd /d %~dp0 && %PYTHON_EXE% -m uvicorn app.main:app --port 8000"

timeout /t 3 >nul

echo [2/2] Opening Frontend...
start "" "%~dp0frontend\index.html"

echo.
echo ========================================
echo ✓ Application Launched!
echo ========================================
echo.
echo API Server: http://127.0.0.1:8000
echo Documentation: http://127.0.0.1:8000/docs
echo Frontend: Will open in your default browser
echo.
echo Press any key to close this window...
echo (The API server will keep running in a separate window)
pause >nul
