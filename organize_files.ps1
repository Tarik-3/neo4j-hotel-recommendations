# File Organization Script for Neo4j Hotel Recommendations Project

$rootPath = Get-Location

# Ensure directories exist
$docDir = Join-Path $rootPath "docs"
$scriptDir = Join-Path $rootPath "scripts"
$queryDir = Join-Path $rootPath "queries"

foreach ($dir in @($docDir, $scriptDir, $queryDir)) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir | Out-Null
        Write-Host "Created directory: $dir"
    }
}

# Documentation files to move
$docFiles = @(
    "COMPLETE_SETUP_GUIDE.md",
    "FRONTEND_SUMMARY.md",
    "MOROCCO_CAN_SETUP.md",
    "NEO4J_SETUP_GUIDE.md",
    "PROJECT_STATUS.md",
    "QUICK_REFERENCE.md",
    "QUICK_START.md",
    "README.md",
    "TEST_RESULTS.txt"
)

# Move documentation files
foreach ($file in $docFiles) {
    $source = Join-Path $rootPath $file
    if (Test-Path $source) {
        Move-Item -Path $source -Destination $docDir -Force
        Write-Host "Moved: $file -> docs/"
    }
}

Write-Host "`nFile organization complete!"
Write-Host "`nProject structure:"
Write-Host "  /app/              - FastAPI application"
Write-Host "  /frontend/         - HTML/CSS/JavaScript UI"
Write-Host "  /scripts/          - Database setup and testing scripts"
Write-Host "  /docs/             - Documentation files"
Write-Host "  /queries/          - Cypher query files"
Write-Host "  /env/              - Python virtual environment"
Write-Host "  .env              - Environment variables"
Write-Host "  requirements.txt  - Python dependencies"
