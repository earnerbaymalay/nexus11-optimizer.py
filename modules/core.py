import sys
import ctypes
import subprocess
from rich.console import Console

console = Console()

def create_restore_point(desc="Nexus11 Backup"):
    console.print(f"[yellow]Creating System Restore Point: {desc}...[/]")
    try:
        # Enable System Restore first just in case
        subprocess.run(["powershell", "Enable-ComputerRestore -Drive 'C:\'"], capture_output=True)
        
        cmd = f'Checkpoint-Computer -Description "{desc}" -RestorePointType "MODIFY_SETTINGS"'
        result = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True)
        
        if result.returncode == 0:
            console.print("[bold green]✔ Restore Point created successfully.[/]")
        else:
            console.print(f"[bold red]Warning:[/] Restore Point creation failed. {result.stderr}")
    except Exception as e:
        console.print(f"[bold red]Warning:[/] Error during restore point creation: {e}")
