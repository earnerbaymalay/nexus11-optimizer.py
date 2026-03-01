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

def disable_copilot():
    """Disable Windows Copilot AI assistant (Windows 11 23H2+)."""
    console.print("[bold magenta]:: COPILOT KILLER ::[/]")
    apply_registry_key(winreg.HKEY_CURRENT_USER, r"Software\Policies\Microsoft\Windows\WindowsCopilot", "TurnOffWindowsCopilot", 1)
    apply_registry_key(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\WindowsCopilot", "TurnOffWindowsCopilot", 1)
    # Hide Copilot taskbar button
    apply_registry_key(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", "ShowCopilotButton", 0)
    console.print("[green]✔ Copilot Disabled & Taskbar Button Hidden[/]")

def disable_recall():
    """Disable Windows Recall AI screenshot feature (Windows 11 24H2+)."""
    console.print("[bold magenta]:: RECALL BLOCKER ::[/]")
    apply_registry_key(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\WindowsAI", "AllowRecallEnablement", 0)
    apply_registry_key(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\WindowsAI", "DisableAIDataAnalysis", 1)
    console.print("[green]✔ Windows Recall (AI Snapshot) Blocked[/]")

def disable_bing_search():
    """Remove Bing search from the Win11 Start Menu."""
    console.print("[bold magenta]:: BING SEARCH REMOVER ::[/]")
    apply_registry_key(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Policies\Microsoft\Windows\Explorer", "DisableSearchBoxSuggestions", 1)
    apply_registry_key(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Search", "BingSearchEnabled", 0)
    console.print("[green]✔ Bing Search in Start Menu Disabled[/]")

def disable_teams_chat():
    """Remove Teams Chat icon from Win11 taskbar and disable autostart."""
    console.print("[bold magenta]:: TEAMS CHAT REMOVER ::[/]")
    # Hide from taskbar
    apply_registry_key(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", "TaskbarMn", 0)
    # Disable autostart
    subprocess.run(
        'reg delete "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run" /v "com.squirrel.Teams.Teams" /f',
        shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    console.print("[green]✔ Teams Chat Hidden & Autostart Disabled[/]")
