import subprocess
from rich.console import Console

console = Console()

def run_deep_clean():
    console.print("[bold red]:: DEEP SYSTEM CLEANUP ::[/]")
    commands = [
        ("CleanMgr", "cleanmgr /sagerun:1"),
        ("WinSxS Cleanup", "dism /online /cleanup-image /startcomponentcleanup"),
        ("Temp Files", "del /q/f/s %TEMP%\*"),
        ("Upgrade Logs", "del /q/f/s C:\Windows\Logs\*")
    ]
    for name, cmd in commands:
        console.print(f"[dim]Executing: {name}...[/]")
        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        console.print(f"  [green]✔ {name} Complete[/]")
