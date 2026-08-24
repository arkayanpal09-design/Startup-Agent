$PSScriptRootLocation = Split-Path -Parent $PSScriptRoot
$ProjectRoot = $PSScriptRootLocation

$PythonExe = "$ProjectRoot\backend\.venv\Scripts\python.exe"
$StartupScript = "$ProjectRoot\backend\startup.py"

Write-Host "Running manual start execution of NOVA Startup Workflow..." -ForegroundColor Cyan

if (-not (Test-Path "$PythonExe")) {
    Write-Host "ERROR: Python environment not found." -ForegroundColor Red
    exit 1
}

& $PythonExe $StartupScript

Write-Host "`nTest Execution Complete. Check Activity Logs for verification." -ForegroundColor Green
