$PSScriptRootLocation = Split-Path -Parent $PSScriptRoot
$ProjectRoot = $PSScriptRootLocation

$PythonVirtualEnv = "$ProjectRoot\backend\.venv"
$PythonExe = "$PythonVirtualEnv\Scripts\python.exe"
$StartupScript = "$ProjectRoot\backend\startup.py"

Write-Host "Installing NOVA Personal PC Agent..." -ForegroundColor Cyan

if (-not (Test-Path "$PythonExe")) {
    Write-Host "ERROR: Python virtual environment not found at $PythonExe" -ForegroundColor Red
    Write-Host "Please ensure the backend exists and requirements are correctly installed."
    exit 1
}

if (-not (Test-Path "$StartupScript")) {
    Write-Host "ERROR: Startup script not found at $StartupScript" -ForegroundColor Red
    exit 1
}

$Action = New-ScheduledTaskAction -Execute "$PythonExe" -Argument "$StartupScript"
$Trigger = New-ScheduledTaskTrigger -AtLogOn
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -ExecutionTimeLimit (New-TimeSpan -Hours 2)

$Principal = New-ScheduledTaskPrincipal -LogonType Interactive -RunLevel LeastPrivilege

Register-ScheduledTask -TaskName "NOVA Personal PC Agent" -Action $Action -Trigger $Trigger -Principal $Principal -Settings $Settings -Force | Out-Null

Write-Host "Success! The scheduled task 'NOVA Personal PC Agent' has been installed." -ForegroundColor Green
