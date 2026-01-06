# Hotel Recommendation API - Quick Start Script
# This script helps you start the API server easily

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "Hotel Recommendation API - Quick Start" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# Find Python executable
$pythonExe = "C:/Users/tarik/AppData/Local/Programs/Python/Python313/python.exe"

# Test Neo4j connection first
Write-Host "Testing Neo4j connection..." -ForegroundColor Yellow
$testResult = & $pythonExe test_connection.py 2>&1

if ($testResult -match "Connection successful") {
    Write-Host "✓ Neo4j connection successful!" -ForegroundColor Green
    Write-Host "`nStarting API server in LIVE mode (with Neo4j database)..." -ForegroundColor Green
    Write-Host "Press Ctrl+C to stop the server`n" -ForegroundColor Yellow
    & $pythonExe -m uvicorn app.main:app --port 8000 --reload
}
else {
    Write-Host "✗ Could not connect to Neo4j database" -ForegroundColor Red
    Write-Host "API will NOT start in mock mode. Please fix the Neo4j connection." -ForegroundColor Red
    Write-Host "See docs/NEO4J_SETUP_GUIDE.md and verify .env credentials." -ForegroundColor Yellow
    Exit 1
}
