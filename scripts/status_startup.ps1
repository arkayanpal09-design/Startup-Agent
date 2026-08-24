$TaskName = "NOVA Personal PC Agent"

Write-Host "NOVA Task Status" -ForegroundColor Cyan
Write-Host "==========================="

$Task = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue

if ($null -eq $Task) {
    Write-Host "NOVA startup task is not installed."
} else {
    $TaskInfo = Get-ScheduledTaskInfo -TaskName $TaskName
    Write-Host "Task Name     : $($Task.TaskName)"
    Write-Host "Task Exists   : True"
    Write-Host "Task State    : $($Task.State)"
    Write-Host "Trigger       : $($Task.Triggers[0].ToString())"
    Write-Host "Action        : $($Task.Actions[0].Execute) $($Task.Actions[0].Arguments)"
    Write-Host "Last Run Time : $($TaskInfo.LastRunTime)"
    Write-Host "Last Result   : $($TaskInfo.LastTaskResult)"
}
Write-Host "==========================="
