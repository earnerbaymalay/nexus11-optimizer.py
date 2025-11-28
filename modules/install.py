import json
import subprocess
import os
from rich.console import Console

console = Console()

def install_essentials():
    config_path = "config/essential_apps.json"
    if not os.path.exists(config_path):
        return

    with open(config_path, 'r') as f:
        apps = json.load(f)

    console.print(f"[bold cyan]Installing {len(apps)} essential apps via Winget...[/]")
    for app in apps:
        name = app.get('name', 'Unknown')
        app_id = app.get('id')
        console.print(f"[dim]Installing {name}...[/]")
        cmd = f"winget install --id {app_id} -e --silent --accept-package-agreements --accept-source-agreements"
        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL)
    
    console.print("[bold green]✔ Installation Complete[/]")
