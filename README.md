<div align="center">

# 🚀 Nexus11 Optimizer
**The Hybrid Windows 11 Optimization Suite (2025 Edition)**

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows_11_24H2-0078D6?style=for-the-badge&logo=windows)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Nexus11** is a modular, hybrid optimization toolkit. It combines the raw power of PowerShell for system management with the modern, safe interface of Python. 
Designed for **Windows 11 24H2**, it targets Bloatware, AI Tracking, and Latency.

[Features](#-key-features) • [Installation](#-installation) • [Usage](#-usage)

</div>

---

## ✨ Key Features

### 🧠 AI & Privacy Killer
* **Recall Blocker:** Disables the controversial "Recall" screenshotting feature (24H2).
* **Copilot Remover:** Registry-level disable of Windows Copilot.
* **Telemetry Shield:** Blocks data collection services and Advertising IDs.

### ⚡ Performance & Gaming
* **Gaming Mode:** Auto-installs **Visual C++ Runtimes (2015-2022)** and enables the "Ultimate Performance" power plan.
* **Network Boost:** Sets DNS to Cloudflare (1.1.1.1) and removes network throttling.
* **Service Optimizer:** Safely disables background services (Fax, Retail Demo, Maps) to free RAM.

### 🧹 Deep Cleaning
* **WinSxS Cleaner:** Analyze and compress the Windows Component Store to free GBs of space.
* **Edge Debloat:** Stops Edge "Startup Boost" and background extensions.
* **Smart Debloat:** Removes pre-installed junk (Candy Crush, Disney+) based on `config/bloatware.json`.

### 📦 App Manager
* **Winget Installer:** Installs essential apps (Chrome, Steam, VS Code, etc.) defined in `config/essential_apps.json`.

---

## 📥 Installation

1.  **Clone the Repo**
    ```bash
    git clone [https://github.com/earnerbaymalay/Nexus11-Optimizer.py](https://github.com/earnerbaymalay/Nexus11-Optimizer.py)
    cd Nexus11-Optimizer
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Usage

**⚠️ Note:** You must run this tool as **Administrator**.

1.  Open your terminal (CMD or PowerShell) as Admin.
2.  Run the main script:
    ```bash
    python main.py
    ```
3.  **Safety First:** The script automatically prompts to create a **System Restore Point** before making changes.

---

## ⚙️ Configuration

* **Bloatware Removal:** Edit `config/bloatware.json`
* **App Installer:** Edit `config/essential_apps.json`

---
<div align="center">
Made with ❤️ for the Windows Community
</div>

