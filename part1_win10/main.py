"""
NEXUS OPTIMIZER — PART 1: WINDOWS 10
======================================
Targeted optimizations for Windows 10 (builds 1903–21H2).
Run as Administrator.
"""
import sys
import os
import ctypes
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

from modules import monitor, tweaks_win10, debloat, core, ai_win10, install, cleaner, services, gaming

console = Console()

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def print_header():
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print(monitor.generate_hud_panel())

def main_menu():
    print_header()

    grid = """
[bold cyan]-- CORE ACTIONS --[/]              [bold magenta]-- TWEAKS & FIXES --[/]
[1] Install Essential Apps      [5] Gaming Mode (Power + VC++ Install)
[2] Deep System Clean           [6] Privacy Shield (Telemetry + AdID)
[3] Debloat Apps (Win10 List)   [7] Cortana & AI Bloat Killer
[4] Service Optimizer           [8] Network Boost (DNS + Throttling)

[bold yellow]-- WIN10 EXTRAS --[/]
[9] Debloat Edge (Kill Startup)
[A] Win10 UI Tweaks (Tray, Startup Delay, Tablet Mode)
[B] Kill News & Interests Widget
[C] Disable OneDrive Autostart
[0] [bold red]RUN ALL (Recommended)[/]
[Q] Exit
    """
    console.print(Panel(grid, title="[bold white]NEXUS // WINDOWS 10 OPTIMIZER[/]", border_style="cyan"))
    return Prompt.ask(
        "[bold]SELECT OPTION >>[/]",
        choices=["1","2","3","4","5","6","7","8","9","A","a","B","b","C","c","0","q","Q"]
    )

def main():
    if not is_admin():
        console.print("[bold red]CRITICAL ERROR:[/] This tool must run as Administrator.")
        console.print("Right-click the terminal and select 'Run as Administrator'.")
        console.input("Press Enter to exit...")
        sys.exit(1)

    print_header()
    if Prompt.ask("[yellow]Create System Restore Point before starting?[/]", choices=["y", "n"], default="y") == "y":
        core.create_restore_point("Nexus-Win10 Backup")

    while True:
        try:
            choice = main_menu().upper()

            if choice == "Q":
                sys.exit()

            run_all = (choice == "0")

            if choice == "1" or run_all:
                install.install_essentials()

            if choice == "2" or run_all:
                cleaner.run_deep_clean()

            if choice == "3" or run_all:
                debloat.run_debloater()

            if choice == "4" or run_all:
                keep_xbox = True
                if choice == "4":
                    keep_xbox = Prompt.ask("Keep Xbox Services (Game Pass)?", choices=["y","n"], default="y") == "y"
                services.disable_services(keep_xbox=keep_xbox)

            if choice == "5" or run_all:
                tweaks_win10.optimize_gaming()
                gaming.install_vc_redist()

            if choice == "6" or run_all:
                tweaks_win10.optimize_privacy()

            if choice == "7" or run_all:
                ai_win10.disable_cortana()

            if choice == "8" or run_all:
                tweaks_win10.optimize_network()
                tweaks_win10.optimize_dns(provider="cloudflare")

            if choice == "9" or run_all:
                tweaks_win10.debloat_edge()

            if choice == "A" or run_all:
                tweaks_win10.apply_win10_ui_tweaks()

            if choice == "B" or run_all:
                ai_win10.disable_news_and_interests()

            if choice == "C" or run_all:
                ai_win10.disable_onedrive_autostart()
                ai_win10.disable_meet_now()

            console.input("\n[dim italic]Press Enter to return to menu...[/]")

        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit()
        except Exception as e:
            console.print(f"[bold red]An error occurred: {e}[/]")
            console.input("Press Enter to continue...")

if __name__ == "__main__":
    main()
