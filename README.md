# ? Nexus Optimizer (v1.1)

A modular Windows optimization toolkit designed to debloat, harden privacy, and boost performance for Windows 10 and Windows 11. This tool combines Python's logic with PowerShell's system-level access to clean your OS.

---

## ?? Setup Guide (For New Systems)

If you have a fresh Windows installation with nothing installed, follow these steps exactly:

### 1. Install Python
*   **Download:** Go to [Python.org](https://www.python.org/downloads/) and download the latest Windows installer.
*   **CRITICAL:** When installing, you **must** check the box that says **"Add Python to PATH"**. If you don't do this, the script won't run.

### 2. Configure Windows Permissions
Windows blocks scripts by default. To allow this tool to work:
1. Right-click your **Start Menu** and select **Terminal (Admin)** or **PowerShell (Admin)**.
2. Paste this command and hit Enter:
   \Set-ExecutionPolicy RemoteSigned -Scope CurrentUser\
3. Type \Y\ and hit Enter.

### 3. Install Required Libraries
Open your Command Prompt (cmd) and run this command:
\\\ash
pip install rich psutil
\\\

### 4. Download & Run
1. Click the green **Code** button at the top of this GitHub page and select **Download ZIP**.
2. Extract the ZIP file to a folder on your Desktop.
3. Open the folder, right-click \launcher.py\ (or \main.py\), and select **Run with Python**.

---

## ??? Main Features

| Category | Description |
| :--- | :--- |
| **Privacy** | Disables Telemetry, Diagnostic Data, and Advertising IDs. |
| **Debloat** | Removes pre-installed junk like Candy Crush and Bing Search. |
| **Performance** | Optimizes power plans and disables unnecessary startup services. |
| **Win 11 Special** | Disables "Recall," Copilot, and restores classic Right-Click menu. |

---

## ?? Important Safety Info
*   **Administrator Rights:** This tool requires Administrator privileges.
*   **System Restore:** The script will attempt to create a System Restore point. **Do not skip this.**
*   **Modules:** Use \part1_win10\ for Win10 and \part2_win11\ for Win11.

---

## ?? Disclaimer
This tool makes significant changes to the Windows Registry. Use at your own risk. Always back up your important files before running optimization scripts.
