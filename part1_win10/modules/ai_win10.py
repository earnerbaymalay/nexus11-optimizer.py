import winreg
import subprocess
from rich.console import Console

console = Console()

def apply_registry_key(hive, path, name, value, value_type=winreg.REG_DWORD):
    try:
        winreg.CreateKey(hive, path)
        key = winreg.OpenKey(hive, path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, name, 0, value_type, value)
        winreg.CloseKey(key)
        return True
    except Exception as e:
        console.print(f"[red]Failed to set {name}: {e}[/]")
        return False

def disable_cortana():
    """Disable Cortana search assistant (Windows 10 specific)."""
    console.print("[bold magenta]:: CORTANA KILLER ::[/]")
    # Disable Cortana via policy
    apply_registry_key(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\Windows Search", "AllowCortana", 0)
    apply_registry_key(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\Windows Search", "AllowCortanaAboveLock", 0)
    apply_registry_key(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\Windows Search", "DisableWebSearch", 1)
    apply_registry_key(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\Windows Search", "ConnectedSearchUseWeb", 0)
    # Disable Bing search in Start Menu
    apply_registry_key(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Search", "BingSearchEnabled", 0)
    apply_registry_key(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Search", "CortanaConsent", 0)
    console.print("[green]✔ Cortana & Bing Search Disabled[/]")

def disable_news_and_interests():
    """Remove the News and Interests widget from the Win10 taskbar."""
    console.print("[bold magenta]:: NEWS & INTERESTS REMOVER ::[/]")
    apply_registry_key(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\Windows Feeds", "EnableFeeds", 0)
    apply_registry_key(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Feeds", "ShellFeedsTaskbarViewMode", 2)
    console.print("[green]✔ News & Interests Widget Removed[/]")

def disable_meet_now():
    """Remove the Meet Now (Skype) button from Win10 taskbar."""
    console.print("[bold magenta]:: MEET NOW REMOVER ::[/]")
    apply_registry_key(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer", "HideSCAMeetNow", 1)
    console.print("[green]✔ Meet Now Button Hidden[/]")

def disable_onedrive_autostart():
    """Stop OneDrive from launching with Windows."""
    console.print("[bold magenta]:: ONEDRIVE AUTOSTART KILL ::[/]")
    subprocess.run(
        'reg delete "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run" /v "OneDrive" /f',
        shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    apply_registry_key(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\OneDrive", "DisableFileSyncNGSC", 1)
    console.print("[green]✔ OneDrive Autostart Disabled[/]")
