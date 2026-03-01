"""
NEXUS OPTIMIZER — PART 2: WINDOWS 11
======================================
Targeted optimizations for Windows 11 (21H2+, including 23H2/24H2).
Run as Administrator.
"""
import sys
import os
import ctypes
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

from modules import monitor, tweaks_win11, debloat, core, ai_win11, install, cleaner, services, gaming

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
[1] Install Essential Apps      [5] Gaming Mode (Power + HAGS + VC++)
[2] Deep System Clean           [6] Privacy Shield (Telemetry + Ads)
[3] Debloat Apps (Win11 List)   [7] AI Killer (Copilot + Recall + Bing)
[4] Service Optimizer           [8] Network Boost (DNS + Throttling)

[bold yellow]-- WIN11 EXCLUSIVES --[/]
[9] Debloat Edge (AI Sidebar + Startup Boost)
[A] Restore Classic Right-Click Menu
[B] Align Taskbar Left + Hide Search
[C] Disable Widgets Panel
[D] Kill Teams Chat
[E] Disable Snap Layout Suggestions
[0] [bold red]RUN ALL (Recommended)[/]
[Q] Exit
    """
    console.print(Panel(grid, title="[bold white]NEXUS // WINDOWS 11 OPTIMIZER[/]", border_style="magenta"))
    return Prompt.ask(
        "[bold]SELECT OPTION >>[/]",
        choices=["1","2","3","4","5","6","7","8","9","A","a","B","b","C","c","D","d","E","e","0","q","Q"]
    )

def main():
    if not is_admin():
        console.print("[bold red]CRITICAL ERROR:[/] This tool must run as Administrator.")
        console.print("Right-click the terminal and select 'Run as Administrator'.")
        console.input("Press Enter to exit...")
        sys.exit(1)

    print_header()
    if Prompt.ask("[yellow]Create System Restore Point before starting?[/]", choices=["y", "n"], default="y") == "y":
        core.create_restore_point("Nexus-Win11 Backup")

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
                tweaks_win11.optimize_gaming()
                gaming.install_vc_redist()

            if choice == "6" or run_all:
                tweaks_win11.optimize_privacy()

            if choice == "7" or run_all:
                ai_win11.disable_copilot()
                ai_win11.disable_recall()
                ai_win11.disable_bing_search()

            if choice == "8" or run_all:
                tweaks_win11.optimize_network()
                tweaks_win11.optimize_dns(provider="cloudflare")

            if choice == "9" or run_all:
                tweaks_win11.debloat_edge()

            if choice == "A" or run_all:
                tweaks_win11.restore_classic_context_menu()

            if choice == "B" or run_all:
                tweaks_win11.align_taskbar_left()
                tweaks_win11.hide_search_taskbar()

            if choice == "C" or run_all:
                tweaks_win11.disable_widgets()

            if choice == "D" or run_all:
                ai_win11.disable_teams_chat()

            if choice == "E" or run_all:
                tweaks_win11.disable_snap_suggestions()

            console.input("\n[dim italic]Press Enter to return to menu...[/]")

        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit()
        except Exception as e:
            console.print(f"[bold red]An error occurred: {e}[/]")
            console.input("Press Enter to continue...")

if __name__ == "__main__":
    main()
