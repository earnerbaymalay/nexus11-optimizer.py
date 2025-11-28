import subprocess
import os
from rich.console import Console

console = Console()

def install_vc_redist():
    console.print("[bold cyan]:: INSTALLING VISUAL C++ RUNTIMES ::[/]")
    urls = ["https://aka.ms/vs/17/release/vc_redist.x64.exe", "https://aka.ms/vs/17/release/vc_redist.x86.exe"]
    temp = os.environ["TEMP"]
    
    for url in urls:
        name = url.split("/")[-1]
        path = os.path.join(temp, name)
        console.print(f"[dim]Downloading {name}...[/]")
        subprocess.run(f"powershell -Command \"Invoke-WebRequest -Uri '{url}' -OutFile '{path}'\"", shell=True)
        console.print(f"[dim]Installing {name}...[/]")
        subprocess.run([path, "/install", "/quiet", "/norestart"])
        
    console.print("[green]✔ Visual C++ Runtimes Updated[/]")
