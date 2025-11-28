import json
import os
import subprocess
from rich.console import Console

console = Console()

def run_debloater():
    config_path = "config/bloatware.json"
    if not os.path.exists(config_path):
        console.print("[red]Config file not found.[/]")
        return

    with open(config_path, 'r') as f:
        apps = json.load(f)

    console.print(f"[bold cyan]Removing {len(apps)} bloatware apps...[/]")
    apps_str = ','.join([f"'{app}'" for app in apps])
    
    ps_script = f"""
    $apps = @({apps_str})
    foreach ($app in $apps) {{
        Write-Host "Removing $app..."
        Get-AppxPackage -Name $app -ErrorAction SilentlyContinue | Remove-AppxPackage -AllUsers -ErrorAction SilentlyContinue
    }}
    """
    subprocess.run(["powershell", "-Command", ps_script], shell=True)
    console.print("[bold green]✔ Debloat Sequence Complete[/]")
