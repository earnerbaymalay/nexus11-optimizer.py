import psutil
import time
from datetime import datetime
from rich.panel import Panel
from rich.table import Table
from rich import box

def get_system_stats():
    try:
        cpu_usage = psutil.cpu_percent(interval=0)
        ram = psutil.virtual_memory()
        boot_time = datetime.fromtimestamp(psutil.boot_time())
        uptime = datetime.now() - boot_time
        uptime_str = str(uptime).split('.')[0]

        return {
            "cpu": cpu_usage,
            "ram_percent": ram.percent,
            "ram_used": round(ram.used / (1024**3), 2),
            "ram_total": round(ram.total / (1024**3), 2),
            "uptime": uptime_str
        }
    except Exception:
        return {
            "cpu": 0, "ram_percent": 0, "ram_used": 0, "ram_total": 0, "uptime": "N/A"
        }

def generate_hud_panel():
    stats = get_system_stats()
    grid = Table.grid(expand=True)
    grid.add_column(justify="center", ratio=1)
    grid.add_column(justify="center", ratio=1)
    grid.add_column(justify="center", ratio=1)

    cpu_color = "green" if stats['cpu'] < 50 else "yellow" if stats['cpu'] < 80 else "red"
    ram_color = "green" if stats['ram_percent'] < 70 else "yellow"

    grid.add_row(
        f"[bold white]CPU Load[/]\n[{cpu_color}]{stats['cpu']}%[/]",
        f"[bold white]RAM Usage[/]\n[{ram_color}]{stats['ram_percent']}%[/]\n[dim]({stats['ram_used']}GB / {stats['ram_total']}GB)[/]",
        f"[bold white]System Uptime[/]\n[cyan]{stats['uptime']}[/]"
    )

    return Panel(grid, title="[bold cyan]NEXUS-11 // SYSTEM MONITOR[/]", border_style="cyan", box=box.ROUNDED)
