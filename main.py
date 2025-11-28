import sys
import os
import ctypes
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.layout import Layout
# Import Modules
from modules import monitor, tweaks, debloat, core, ai, install, cleaner, services, gaming

console = Console()

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def print_header():
    # Force Hard Clear for Windows Terminals
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print(monitor.generate_hud_panel())

def main_menu():
    print_header()
    
    grid = """
[bold cyan]-- CORE ACTIONS --[/]              [bold magenta]-- TWEAKS & FIXES --[/]
[1] Install Essential Apps      [5] Gaming Mode (Power + VC++ Install)
[2] Deep System Clean           [6] Privacy Shield (Telemetry + AdID)
[3] Debloat Apps (Config)       [7] AI Killer (Copilot + Recall)
[4] Service Optimizer           [8] Network Boost (DNS + Throttling)

[bold yellow]-- EXTRAS --[/]
[9] Debloat Edge (Kill Startup)
[0] [bold red]RUN ALL (Recommended)[/]
[Q] Exit
    """
    console.print(Panel(grid, title="[bold white]MAIN MENU[/]", border_style="cyan"))
    return Prompt.ask("[bold]SELECT OPTION >>[/]", choices=["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "q", "Q"])

def main():
    if not is_admin():
        console.print("[bold red]CRITICAL ERROR:[/] This tool must run as Administrator.")
        console.print("Right-click the terminal and select 'Run as Administrator'.")
        console.input("Press Enter to exit...")
        sys.exit(1)

    # Auto-Restore Point Check
    print_header()
    if Prompt.ask("[yellow]Create System Restore Point before starting?[/]", choices=["y", "n"], default="y") == "y":
        core.create_restore_point()

    while True:
        try:
            choice = main_menu()
            
            if choice.lower() == "q":
                sys.exit()

            # Batch Execution (0) or Individual
            run_all = (choice == "0")

            if choice == "1" or run_all:
                install.install_essentials()
            
            if choice == "2" or run_all:
                cleaner.run_deep_clean()
                
            if choice == "3" or run_all:
                debloat.run_debloater()
                
            if choice == "4" or run_all:
                # If running all, default to keeping Xbox to be safe
                keep_xbox = True
                if choice == "4":
                    keep_xbox = Prompt.ask("Keep Xbox Services (Game Pass)?", choices=["y", "n"], default="y") == "y"
                services.disable_services(keep_xbox=keep_xbox)
                
            if choice == "5" or run_all:
                tweaks.optimize_gaming() 
                gaming.install_vc_redist()
                
            if choice == "6" or run_all:
                tweaks.optimize_privacy()
                
            if choice == "7" or run_all:
                ai.disable_copilot()
                ai.disable_recall()
                
            if choice == "8" or run_all:
                tweaks.optimize_network()
                tweaks.optimize_dns(provider="cloudflare")
                
            if choice == "9" or run_all:
                tweaks.debloat_edge()
            
            console.input("\n[dim italic]Press Enter to return to menu...[/]")
            
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit()
        except Exception as e:
            console.print(f"[bold red]An error occurred: {e}[/]")
            console.input("Press Enter to continue...")

if __name__ == "__main__":
    main()
