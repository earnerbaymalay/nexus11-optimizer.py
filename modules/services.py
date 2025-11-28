import subprocess
from rich.console import Console

console = Console()
SAFE_SERVICES = ["DiagTrack", "dmwappushservice", "MapsBroker", "lfsvc", "SharedAccess", "XblAuthManager", "XblGameSave", "XboxNetApiSvc", "RetailDemo", "TroubleshootingSvc"]

def disable_services(keep_xbox=False):
    console.print("[bold magenta]:: SERVICE OPTIMIZER ::[/]")
    target = SAFE_SERVICES[:]
    if keep_xbox:
        target = [s for s in target if "Xbox" not in s and "Xbl" not in s]

    ps_script = """
    $services = @(
        {SERVICE_LIST}
    )
    foreach ($service in $services) {{
        Set-Service -Name $service -StartupType Disabled -ErrorAction SilentlyContinue
        Stop-Service -Name $service -Force -ErrorAction SilentlyContinue
    }}
    """.replace("{SERVICE_LIST}", ",".join([f"'{s}'" for s in target]))
    
    subprocess.run(["powershell", "-Command", ps_script], shell=True)
    console.print(f"[green]✔ Optimized Background Services[/]")
