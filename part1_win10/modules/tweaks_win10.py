import winreg
import subprocess
from rich.console import Console

console = Console()

def apply_registry_tweak(hive, path, name, value, value_type=winreg.REG_DWORD):
    try:
        winreg.CreateKey(hive, path)
        key = winreg.OpenKey(hive, path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, name, 0, value_type, value)
        winreg.CloseKey(key)
        return True
    except Exception as e:
        console.print(f"[red]Failed to set {name}: {e}[/]")
        return False

def optimize_gaming():
    console.print("[bold magenta]:: GAMING & PERFORMANCE OVERDRIVE (WIN10) ::[/]")
    # Network Throttling
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile", "NetworkThrottlingIndex", 0xFFFFFFFF)
    # System Responsiveness
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile", "SystemResponsiveness", 0)
    # GameDVR (works on Win10 too)
    apply_registry_tweak(winreg.HKEY_CURRENT_USER, r"System\GameConfigStore", "GameDVR_Enabled", 0)
    apply_registry_tweak(winreg.HKEY_CURRENT_USER, r"System\GameConfigStore", "GameDVR_FSEBehaviorMode", 2)
    # Win10 Ultimate Performance plan
    subprocess.run('powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61', shell=True, stdout=subprocess.DEVNULL)
    subprocess.run('powercfg -setactive e9a42b02-d5df-448d-aa00-03f14749eb61', shell=True, stdout=subprocess.DEVNULL)
    # Disable hardware-accelerated GPU scheduling on Win10 (feature is buggy pre-Win11)
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers", "HwSchMode", 2)
    console.print("[green]✔ Ultimate Performance Plan Enabled (Win10)[/]")

def optimize_privacy():
    console.print("[bold magenta]:: PRIVACY SHIELD (WIN10) ::[/]")
    # Telemetry — set to Security (0) level
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\DataCollection", "AllowTelemetry", 0)
    # Advertising ID
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\AdvertisingInfo", "Enabled", 0)
    # Disable Cortana (also done in ai_win10.py, belt-and-suspenders)
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\Windows Search", "AllowCortana", 0)
    # Disable Bing Search in Start
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\Explorer", "DisableSearchBoxSuggestions", 1)
    # Disable activity history (timeline)
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\System", "EnableActivityFeed", 0)
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\System", "PublishUserActivities", 0)
    # Disable location tracking
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\LocationAndSensors", "DisableLocation", 1)
    console.print("[green]✔ Telemetry, Ads, Cortana & Activity History Blocked[/]")

def optimize_network():
    console.print("[bold magenta]:: NETWORK OPTIMIZATION (WIN10) ::[/]")
    commands = [
        "netsh int tcp set global autotuninglevel=normal",
        "netsh int tcp set global rss=enabled",
        "netsh int tcp set global chimney=disabled",
        "ipconfig /flushdns"
    ]
    for cmd in commands:
        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL)
    console.print("[green]✔ DNS Flushed & TCP Globals Optimized[/]")

def optimize_dns(provider="cloudflare"):
    console.print(f"[bold magenta]:: DNS OPTIMIZER ({provider.upper()}) ::[/]")
    dns_map = {"cloudflare": ("1.1.1.1", "1.0.0.1"), "google": ("8.8.8.8", "8.8.4.4")}
    primary, secondary = dns_map.get(provider, dns_map["cloudflare"])
    ps_script = f"""
    $wmi = Get-WmiObject -Class Win32_NetworkAdapterConfiguration | Where-Object {{ $_.IPEnabled -eq $true }}
    foreach ($adapter in $wmi) {{
        $adapter.SetDNSServerSearchOrder(@("{primary}", "{secondary}")) | Out-Null
    }}
    """
    subprocess.run(["powershell", "-Command", ps_script], shell=True)
    console.print(f"[green]✔ DNS set to {primary} on active adapters[/]")

def debloat_edge():
    console.print("[bold magenta]:: EDGE DEBLOAT (WIN10) ::[/]")
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Edge", "StartupBoostEnabled", 0)
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Edge", "StandaloneHubsSidebarEnabled", 0)
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Edge", "BackgroundModeEnabled", 0)
    console.print("[green]✔ Edge Startup Boost & Background Processes Killed[/]")

def apply_win10_ui_tweaks():
    """Windows 10 specific UI/UX improvements."""
    console.print("[bold magenta]:: WIN10 UI TWEAKS ::[/]")
    # Show all tray icons
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer", "EnableAutoTray", 0)
    # Disable startup delay
    apply_registry_tweak(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Serialize", "StartupDelayInMSec", 0)
    # Disable auto-restart after updates during active hours
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU", "NoAutoRebootWithLoggedOnUsers", 1)
    # Disable tablet mode auto-switch
    apply_registry_tweak(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\ImmersiveShell", "SignInMode", 1)
    console.print("[green]✔ Win10 UI Tweaks Applied[/]")
