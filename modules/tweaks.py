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
    console.print("[bold magenta]:: GAMING & PERFORMANCE OVERDRIVE ::[/]")
    # Network Throttling
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile", "NetworkThrottlingIndex", 0xFFFFFFFF)
    # System Responsiveness
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile", "SystemResponsiveness", 0)
    # GameDVR
    apply_registry_tweak(winreg.HKEY_CURRENT_USER, r"System\GameConfigStore", "GameDVR_Enabled", 0)
    # Ultimate Performance Plan
    subprocess.run('powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61', shell=True, stdout=subprocess.DEVNULL)
    subprocess.run('powercfg -setactive e9a42b02-d5df-448d-aa00-03f14749eb61', shell=True, stdout=subprocess.DEVNULL)
    console.print("[green]✔ Ultimate Performance Plan Enabled[/]")

def optimize_privacy():
    console.print("[bold magenta]:: PRIVACY SHIELD ::[/]")
    # Telemetry
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\DataCollection", "AllowTelemetry", 0)
    # Advertising ID
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\AdvertisingInfo", "Enabled", 0)
    # Disable Cortana Registry
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\Windows Search", "AllowCortana", 0)
    # Disable Bing Search
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\Explorer", "DisableSearchBoxSuggestions", 1)
    console.print("[green]✔ Telemetry, Ads, & Cortana Blocked[/]")

def optimize_network():
    console.print("[bold magenta]:: NETWORK OPTIMIZATION ::[/]")
    commands = ["netsh int tcp set global autotuninglevel=normal", "netsh int tcp set global rss=enabled", "ipconfig /flushdns"]
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
    console.print("[bold magenta]:: EDGE DEBLOAT ::[/]")
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Edge", "StartupBoostEnabled", 0)
    apply_registry_tweak(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Edge", "StandaloneHubsSidebarEnabled", 0)
    console.print("[green]✔ Edge Startup Boost & Background Processes Killed[/]")
