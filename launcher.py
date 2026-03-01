"""
NEXUS OPTIMIZER — SMART LAUNCHER
==================================
Detects Windows version and routes to the correct optimizer:
  Part 1 → Windows 10
  Part 2 → Windows 11
"""
import sys
import os
import subprocess
import ctypes
import platform

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def get_windows_version():
    """Return major Windows version as an integer (10 or 11)."""
    try:
        release = platform.release()
        version = platform.version()
        # Windows 11 reports as release '10' but build >= 22000
        build = int(version.split('.')[2]) if version.count('.') >= 2 else 0
        if build >= 22000:
            return 11
        return 10
    except Exception:
        return 10  # Fallback to Win10

def relaunch_as_admin():
    """Relaunch this script with administrator privileges."""
    script = os.path.abspath(__file__)
    subprocess.run(
        ['powershell', '-Command', f'Start-Process python -ArgumentList \\"{script}\\" -Verb RunAs'],
        shell=True
    )
    sys.exit()

def main():
    if not is_admin():
        print("[!] Not running as Administrator. Relaunching with elevation...")
        relaunch_as_admin()
        return

    win_version = get_windows_version()
    script_dir = os.path.dirname(os.path.abspath(__file__))

    print(f"\n  NEXUS OPTIMIZER — Detected Windows {win_version}")
    print("  " + "─" * 40)

    if win_version == 11:
        target = os.path.join(script_dir, "part2_win11", "main.py")
        print("  Launching: Part 2 — Windows 11 Optimizer\n")
    else:
        target = os.path.join(script_dir, "part1_win10", "main.py")
        print("  Launching: Part 1 — Windows 10 Optimizer\n")

    if not os.path.exists(target):
        print(f"  [ERROR] Target not found: {target}")
        input("  Press Enter to exit...")
        sys.exit(1)

    # Change to the correct part directory so relative imports work
    part_dir = os.path.dirname(target)
    os.chdir(part_dir)
    sys.path.insert(0, part_dir)

    # Execute the correct main
    import runpy
    runpy.run_path(target, run_name="__main__")

if __name__ == "__main__":
    main()
