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
    console.print("[bold magenta]:: GAMING & PERFORMANCE OVERDRIVE (WIN11) ::[/]")
    # Network Throttling
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile", "NetworkThrottlingIndex", 0xFFFFFFFF)
    # System Responsiveness
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile", "SystemResponsiveness", 0)
    # GameDVR
    apply_registry_tweak(winreg.HKEY_CURRENT_USER, r"System\GameConfigStore", "GameDVR_Enabled", 0)
    apply_registry_tweak(winreg.HKEY_CURRENT_USER, r"System\GameConfigStore", "GameDVR_FSEBehaviorMode", 2)
    # Win11 Hardware-Accelerated GPU Scheduling (HAGS) — beneficial on Win11
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\GraphicsDrivers", "HwSchMode", 2)
    # Win11 Ultimate Performance plan
    subprocess.run('powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61', shell=True, stdout=subprocess.DEVNULL)
    subprocess.run('powercfg -setactive e9a42b02-d5df-448d-aa00-03f14749eb61', shell=True, stdout=subprocess.DEVNULL)
    # Disable VBS/HVCI if it's hurting game performance (advanced — user should verify)
    console.print("[yellow]  Note: VBS/HVCI is left enabled. Disable manually if needed for max FPS.[/]")
    console.print("[green]✔ Ultimate Performance Plan Enabled (Win11)[/]")

def optimize_privacy():
    console.print("[bold magenta]:: PRIVACY SHIELD (WIN11) ::[/]")
    # Telemetry
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\DataCollection", "AllowTelemetry", 0)
    # Advertising ID
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\AdvertisingInfo", "Enabled", 0)
    # Disable Start Menu recommendations/suggestions
    apply_registry_tweak(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", "Start_IrisRecommendations", 0)
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\Explorer", "HideRecommendedSection", 1)
    # Activity history
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\System", "EnableActivityFeed", 0)
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\System", "PublishUserActivities", 0)
    # Location
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\LocationAndSensors", "DisableLocation", 1)
    console.print("[green]✔ Telemetry, Ads & Start Recommendations Blocked[/]")

def optimize_network():
    console.print("[bold magenta]:: NETWORK OPTIMIZATION (WIN11) ::[/]")
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
    Get-NetAdapter | Where-Object {{$_.Status -eq 'Up'}} | ForEach-Object {{
        Set-DnsClientServerAddress -InterfaceIndex $_.ifIndex -ServerAddresses ("{primary}","{secondary}")
    }}
    """
    subprocess.run(["powershell", "-Command", ps_script], shell=True)
    console.print(f"[green]✔ DNS set to {primary} (Win11 method)[/]")

def debloat_edge():
    console.print("[bold magenta]:: EDGE DEBLOAT (WIN11) ::[/]")
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Edge", "StartupBoostEnabled", 0)
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Edge", "StandaloneHubsSidebarEnabled", 0)
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Edge", "BackgroundModeEnabled", 0)
    # Disable Edge's sidebar AI Copilot
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Edge", "HubsSidebarEnabled", 0)
    console.print("[green]✔ Edge Startup Boost, Background & AI Sidebar Killed[/]")

def restore_classic_context_menu():
    """Restore the full/classic right-click context menu on Win11."""
    console.print("[bold magenta]:: CLASSIC CONTEXT MENU RESTORE ::[/]")
    apply_registry_tweak(
        winreg.HKEY_CURRENT_USER,
        r"Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32",
        "",
        "",
        winreg.REG_SZ
    )
    console.print("[green]✔ Classic Right-Click Menu Restored (restart Explorer to apply)[/]")

def align_taskbar_left():
    """Move Win11 taskbar icons from center to the classic left-aligned position."""
    console.print("[bold magenta]:: TASKBAR LEFT ALIGN ::[/]")
    apply_registry_tweak(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", "TaskbarAl", 0)
    console.print("[green]✔ Taskbar Aligned Left[/]")

def disable_widgets():
    """Disable the Win11 Widgets panel and taskbar button."""
    console.print("[bold magenta]:: WIDGETS PANEL DISABLER ::[/]")
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Dsh", "AllowNewsAndInterests", 0)
    apply_registry_tweak(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", "TaskbarDa", 0)
    console.print("[green]✔ Widgets Panel & Taskbar Button Disabled[/]")

def disable_snap_suggestions():
    """Turn off Snap Layout overlay (the grid that appears on maximise hover)."""
    console.print("[bold magenta]:: SNAP LAYOUT OVERLAY TOGGLE ::[/]")
    apply_registry_tweak(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", "SnapAssist", 0)
    apply_registry_tweak(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", "EnableSnapBar", 0)
    console.print("[green]✔ Snap Layout Suggestions Disabled[/]")

def hide_search_taskbar():
    """Remove the Search button/box from the Win11 taskbar."""
    console.print("[bold magenta]:: TASKBAR SEARCH HIDE ::[/]")
    # 0 = hidden, 1 = search icon, 2 = search box
    apply_registry_tweak(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Search", "SearchboxTaskbarMode", 0)
    console.print("[green]✔ Taskbar Search Box Hidden[/]")
