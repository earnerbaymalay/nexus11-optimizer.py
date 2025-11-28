# Utility Module for Nexus-11
# Contains all shared UI, logging, and safety functions.

$Script:RestorePointCreated = $false

function Log-ToFile {
    param([string]$Message, [string]$Type = "INFO")
    $TimeStamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $LogLine = "[$TimeStamp] [$Type] $Message"
    Add-Content -Path $Global:NexusConfig.LogFile -Value $LogLine -ErrorAction SilentlyContinue
}

function Draw-Line {
    param([string]$Char = '─', [int]$Length = 70, $Config)
    Write-Host ($Char * $Length) -ForegroundColor $Config.Theme.Border
}

function Write-HUD {
    param($Config)
    Clear-Host
    $Theme = $Config.Theme
    
    # Gather Real-Time Stats
    $osInfo = Get-CimInstance Win32_OperatingSystem
    $os = $osInfo.Caption
    $uptimeSpan = (Get-Date) - $osInfo.LastBootUpTime
    $uptimeStr = "{0}d {1}h {2}m" -f $uptimeSpan.Days, $uptimeSpan.Hours, $uptimeSpan.Minutes
    
    # CPU & RAM Stats
    $cpuLoad = (Get-CimInstance Win32_Processor).LoadPercentage
    $ramUsedGB = [math]::Round(($osInfo.TotalVisibleMemorySize - $osInfo.FreePhysicalMemory) / 1048576, 1)
    $ramTotalGB = [math]::Round($osInfo.TotalVisibleMemorySize / 1048576, 1)
    $ramPerc = if ($ramTotalGB -gt 0) { [math]::Round(($ramUsedGB / $ramTotalGB) * 100, 0) } else { 0 }

    $Banner = @"

  ███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗
  ████╗  ██║██╔════╝╚██╗██╔╝██║   ██║██╔════╝
  ██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗
  ██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║╚════██║
  ██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║
  ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
           :: SYSTEM OPTIMIZATION SUITE ::
"@
    Write-Host $Banner -ForegroundColor $Theme.Title
    Draw-Line '═' -Config $Config
    
    Write-Host "  OS: $os" -NoNewline -ForegroundColor $Theme.Text
    Write-Host "  |  " -NoNewline -ForegroundColor $Theme.Border
    Write-Host "UPTIME: $uptimeStr" -ForegroundColor $Theme.Text
    
    Write-Host "  CPU: $cpuLoad%" -NoNewline -ForegroundColor $Theme.Accent
    Write-Host (" " * (5 - $cpuLoad.ToString().Length)) -NoNewline
    Write-Host "|  " -NoNewline -ForegroundColor $Theme.Border
    Write-Host "RAM: $ramPerc% ($ramUsedGB GB / $ramTotalGB GB)" -ForegroundColor $Theme.Accent
    Draw-Line '─' -Config $Config
}

function Log-Action {
    param([string]$Message, [string]$Status = 'OK', $Config)
    $Theme = $Config.Theme
    
    Start-Sleep -Milliseconds 25
    $TimeStamp = Get-Date -Format 'HH:mm:ss'
    
    Write-Host "  [$TimeStamp] " -NoNewline -ForegroundColor $Theme.Border
    Write-Host "$Message" -NoNewline -ForegroundColor $Theme.Text
    
    $pad = 55 - $Message.Length
    if ($pad -lt 1) { $pad = 1 }
    Write-Host (' ' * $pad) -NoNewline
    
    switch ($Status) {
        'OK'   { Write-Host '[  OK  ]' -ForegroundColor $Theme.Success }
        'SKIP' { Write-Host '[ SKIP ]' -ForegroundColor $Theme.Warn }
        'FAIL' { Write-Host '[ FAIL ]' -ForegroundColor $Theme.Error }
        'DONE' { Write-Host '[ DONE ]' -ForegroundColor $Theme.Title }
        'WAIT' { Write-Host '[ .... ]' -ForegroundColor $Theme.Warn }
    }
    Log-ToFile "$Message - $Status"
}

function Invoke-SystemRestore {
    param($Config)
    if ($Script:RestorePointCreated) { return }
    Write-Host ''
    Write-Host '  :: SAFETY PROTOCOLS' -ForegroundColor $Config.Theme.Title
    Draw-Line '-' -Config $Config
    
    Log-Action 'Initializing VSS' 'WAIT' -Config $Config
    Enable-ComputerRestore -Drive 'C:\' -ErrorAction SilentlyContinue
    try {
        Checkpoint-Computer -Description 'NEXUS_PreOptimize' -RestorePointType 'MODIFY_SETTINGS' -ErrorAction Stop | Out-Null
        Log-Action 'Restore Point Created' 'OK' -Config $Config
        $Script:RestorePointCreated = $true
    } catch {
        Log-Action 'Restore Point Failed (Check System Config)' 'FAIL' -Config $Config
        Log-ToFile "Restore Point Error: $($_.Exception.Message)" "ERROR"
    }
}

Export-ModuleMember -Function Draw-Line, Write-HUD, Log-Action, Log-ToFile, Invoke-SystemRestore
