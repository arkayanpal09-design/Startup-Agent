Write-Host "Uninstalling NOVA Personal PC Agent..." -ForegroundColor Cyan

$TaskName = "NOVA Personal PC Agent"
$TaskExists = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue

if ($TaskExists) {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
    Write-Host "Success! The scheduled task '$TaskName' has been securely removed." -ForegroundColor Green
    Write-Host "None of your files, settings, or Chrome data were deleted."
} else {
    Write-Host "The task '$TaskName' is not installed or previously removed." -ForegroundColor Yellow
}
