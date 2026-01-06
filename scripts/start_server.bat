@echo off
echo ========================================
echo Hotel Recommendation API - Quick Start
echo ========================================
echo.

set PYTHON_EXE=C:\Users\tarik\AppData\Local\Programs\Python\Python313\python.exe

echo Testing Neo4j connection...
%PYTHON_EXE% test_connection.py >nul 2>&1

if %ERRORLEVEL% EQU 0 (
    echo [OK] Neo4j connection successful!
    echo.
    echo Starting API server in LIVE mode with Neo4j database...
    echo Press Ctrl+C to stop the server
    echo.
    echo API will be available at: http://127.0.0.1:8000
    echo Documentation at: http://127.0.0.1:8000/docs
    echo.
    %PYTHON_EXE% -m uvicorn app.main:app --port 8000 --reload
) else (
    echo [WARNING] Could not connect to Neo4j database
    echo.
    echo Starting API server in MOCK mode with sample data...
    echo To fix Neo4j connection, see: NEO4J_SETUP_GUIDE.md
    echo Press Ctrl+C to stop the server
    echo.
    echo API will be available at: http://127.0.0.1:8000
    echo Documentation at: http://127.0.0.1:8000/docs
    echo.
    set USE_MOCK=true
    %PYTHON_EXE% -m uvicorn app.main:app --port 8000 --reload
)
