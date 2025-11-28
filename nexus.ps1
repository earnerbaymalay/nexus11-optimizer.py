<#
.SYNOPSIS
    NEXUS-11 // System Optimization Interface
    v3.1.0 - "Fusion" Build

.DESCRIPTION
    A modular, configurable, and immersive optimization toolkit for Windows 11.
    Features auto-elevation, persistent logging, and a real-time system HUD.

.NOTES
    - AUTO-ELEVATES TO ADMINISTRATOR
#>

# --------------------------------------------------------
# [AUTO-ELEVATION & INITIALIZATION]
# --------------------------------------------------------
if (!([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] 'Administrator')) {
    Start-Process powershell.exe -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File `"$($MyInvocation.MyCommand.Path)`"" -Verb RunAs; Exit
}

# Set script root for reliable pathing
$PSScriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Definition

# Load global configuration and theme
$Global:NexusConfig = @{
    Version = "3.1.0"
    LogFile = "$PSScriptRoot\\Nexus11.log"
    Theme   = @{
        Title = 'Cyan'; Border = 'DarkGray'; Text = 'Gray'; Accent = 'Magenta';
        Success = 'Green'; Warn = 'Yellow'; Error = 'Red'
    }
}

# Import all modules from the 'src/modules' directory
Get-ChildItem -Path "$PSScriptRoot\\src\\modules\\*.psm1" | ForEach-Object { Import-Module $_.FullName -Force }

# --------------------------------------------------------
# [MAIN EXECUTION LOOP]
# --------------------------------------------------------
Start-Transcript -Path $Global:NexusConfig.LogFile -Append -Force | Out-Null
Log-ToFile "Nexus-11 Session Started"

while ($true) {
    Write-HUD -Config $Global:NexusConfig
    $Theme = $Global:NexusConfig.Theme

    # --- Menu Display ---
    Write-Host ''
    Write-Host '  [1] ' -NoNewline -ForegroundColor $Theme.Accent; Write-Host 'EXECUTE FULL SUITE' -ForegroundColor $Theme.Title
    Write-Host '      Run all modules sequentially with safety checks.' -ForegroundColor $Theme.Text; Write-Host ''
    Write-Host '  [2] ' -NoNewline -ForegroundColor $Theme.Accent; Write-Host 'PRIVACY & TELEMETRY' -ForegroundColor 'White'
    Write-Host '  [3] ' -NoNewline -ForegroundColor $Theme.Accent; Write-Host 'GAMING & PERFORMANCE' -ForegroundColor 'White'
    Write-Host '  [4] ' -NoNewline -ForegroundColor $Theme.Accent; Write-Host 'UI & VISUALS' -ForegroundColor 'White'
    Write-Host '  [5] ' -NoNewline -ForegroundColor $Theme.Accent; Write-Host 'DEBLOAT APPS (CONFIGURABLE)' -ForegroundColor 'White'
    Write-Host '  [6] ' -NoNewline -ForegroundColor $Theme.Accent; Write-Host 'STORAGE & CLEANUP' -ForegroundColor 'White'
    Write-Host '  [7] ' -NoNewline -ForegroundColor $Theme.Accent; Write-Host 'NETWORK OPTIMIZER' -ForegroundColor 'White'
    Write-Host ''
    Write-Host '  [Q] ' -NoNewline -ForegroundColor $Theme.Error; Write-Host 'EXIT NEXUS' -ForegroundColor 'White'
    Write-Host ''; Draw-Line '═' -Theme $Theme
    
    if ($Host.UI.RawUI.KeyAvailable) { $null = $Host.UI.RawUI.FlushInputBuffer() }
    $choice = Read-Host '  INPUT >>'
    
    switch ($choice) {
        '1' { 
            $confirm = Read-Host "  [?] Execute FULL SUITE? This is irreversible. (Y/N)"
            if ($confirm -eq 'y') {
                Invoke-SystemRestore -Config $Global:NexusConfig
                Invoke-PrivacyOptimizations -Config $Global:NexusConfig
                Invoke-GamingOptimizations -Config $Global:NexusConfig
                Invoke-UIOptimizations -Config $Global:NexusConfig
                Invoke-AppxDebloat -Config $Global:NexusConfig -ConfigFile "$PSScriptRoot\\config\\bloatware.json"
                Invoke-StorageOptimizations -Config $Global:NexusConfig
                Invoke-NetworkOptimizations -Config $Global:NexusConfig
                Write-Host ''; Log-Action 'ALL TASKS COMPLETED. REBOOT REQUIRED.' 'DONE' -Config $Global:NexusConfig; Pause
            } else {
                Log-Action 'Full Suite Aborted by User.' 'SKIP' -Config $Global:NexusConfig; Start-Sleep -s 2
            }
        }
        '2' { Invoke-SystemRestore -Config $Global:NexusConfig; Invoke-PrivacyOptimizations -Config $Global:NexusConfig; Pause }
        '3' { Invoke-SystemRestore -Config $Global:NexusConfig; Invoke-GamingOptimizations -Config $Global:NexusConfig; Pause }
        '4' { Invoke-SystemRestore -Config $Global:NexusConfig; Invoke-UIOptimizations -Config $Global:NexusConfig; Pause }
        '5' { Invoke-SystemRestore -Config $Global:NexusConfig; Invoke-AppxDebloat -Config $Global:NexusConfig -ConfigFile "$PSScriptRoot\\config\\bloatware.json"; Pause }
        '6' { Invoke-SystemRestore -Config $Global:NexusConfig; Invoke-StorageOptimizations -Config $Global:NexusConfig; Pause }
        '7' { Invoke-SystemRestore -Config $Global:NexusConfig; Invoke-NetworkOptimizations -Config $Global:NexusConfig; Pause }
        'Q' { Log-ToFile "Nexus-11 Session Ended"; Stop-Transcript; Write-Host '  Terminating...' -ForegroundColor $Theme.Error; Break }
        Default { Log-Action 'Invalid Command' 'FAIL' -Config $Global:NexusConfig; Start-Sleep -s 1 }
    }
}
