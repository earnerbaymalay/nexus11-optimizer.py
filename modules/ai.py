import winreg
from rich.console import Console

console = Console()

def apply_registry_key(hive, path, name, value):
    try:
        winreg.CreateKey(hive, path)
        key = winreg.OpenKey(hive, path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, name, 0, winreg.REG_DWORD, value)
        winreg.CloseKey(key)
        return True
    except Exception as e:
        console.print(f"[red]Failed to set {name}: {e}[/]")
        return False

def disable_copilot():
    console.print("[bold magenta]Killing Windows Copilot...[/]")
    apply_registry_key(winreg.HKEY_CURRENT_USER, r"Software\Policies\Microsoft\Windows\WindowsCopilot", "TurnOffWindowsCopilot", 1)
    apply_registry_key(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\WindowsCopilot", "TurnOffWindowsCopilot", 1)
    console.print("[green]✔ Copilot Disabled via Registry[/]")

def disable_recall():
    console.print("[bold magenta]Disabling Windows Recall (Snapshot AI)...[/]")
    apply_registry_key(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Policies\Microsoft\Windows\WindowsAI", "AllowRecallEnablement", 0)
    console.print("[green]✔ Windows Recall Feature Blocked[/]")
