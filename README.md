<div align="center">

# ⚡ Nexus Optimizer
**Dual-Edition Windows Optimization Suite — Win10 & Win11**

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Win10](https://img.shields.io/badge/Part_1-Windows_10-0078D6?style=for-the-badge&logo=windows)
![Win11](https://img.shields.io/badge/Part_2-Windows_11-6264A7?style=for-the-badge&logo=windows11)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A modular, hybrid optimization toolkit. Two editions — each tuned specifically for its Windows version.
Registry tweaks, bloatware removal, privacy hardening, gaming performance — all from one menu.

[Part 1 — Win10](#-part-1--windows-10) • [Part 2 — Win11](#-part-2--windows-11) • [Installation](#-installation) • [Usage](#-usage)

</div>

---

## 🗂️ Project Structure

```
nexus-optimizer/
├── launcher.py              ← Auto-detects Windows version, routes to correct part
├── part1_win10/             ← Windows 10 optimizer
│   ├── main.py
│   ├── modules/
│   │   ├── ai_win10.py      # Cortana, News & Interests, Meet Now, OneDrive
│   │   ├── tweaks_win10.py  # Gaming, Privacy, Network, UI tweaks (Win10)
│   │   ├── debloat.py       # AppX removal
│   │   ├── services.py      # Background service optimizer
│   │   ├── core.py          # Restore point creation
│   │   ├── cleaner.py       # Deep clean (Temp, WinSxS, Logs)
│   │   ├── gaming.py        # VC++ runtime installer
│   │   ├── install.py       # Winget app installer
│   │   └── monitor.py       # Live CPU/RAM HUD
│   └── config/
│       ├── bloatware_win10.json
│       └── essential_apps.json
├── part2_win11/             ← Windows 11 optimizer
│   ├── main.py
│   ├── modules/
│   │   ├── ai_win11.py      # Copilot, Recall, Bing Search, Teams Chat
│   │   ├── tweaks_win11.py  # Gaming (HAGS), Privacy, Taskbar, Widgets, Snap
│   │   ├── debloat.py       # AppX removal
│   │   ├── services.py      # Background service optimizer
│   │   ├── core.py          # Restore point creation
│   │   ├── cleaner.py       # Deep clean
│   │   ├── gaming.py        # VC++ runtime installer
│   │   ├── install.py       # Winget app installer
│   │   └── monitor.py       # Live CPU/RAM HUD
│   └── config/
│       ├── bloatware_win11.json
│       └── essential_apps.json
└── README.md
```

---

## 🪟 Part 1 — Windows 10

Targets Windows 10 versions **1903 through 21H2**.

### Menu Options

| Key | Action |
|-----|--------|
| `1` | Install essential apps via Winget |
| `2` | Deep system clean (Temp, WinSxS, Logs) |
| `3` | Debloat using Win10-specific app list |
| `4` | Disable background services (opt: keep Xbox) |
| `5` | Gaming Mode — Ultimate Performance plan + VC++ |
| `6` | Privacy Shield — Telemetry, Ads, Activity History |
| `7` | Cortana & AI Killer |
| `8` | Network Boost — Cloudflare DNS + TCP tuning |
| `9` | Edge Debloat — Kill startup boost & background |
| `A` | Win10 UI Tweaks — Tray icons, startup delay, tablet mode |
| `B` | Kill News & Interests taskbar widget |
| `C` | Disable OneDrive autostart + Remove Meet Now button |
| `0` | **Run All** |

### Win10-Exclusive Tweaks
- **Cortana disable** — registry policy + BingSearchEnabled kill
- **News & Interests** — taskbar feed widget (ShellFeedsTaskbarViewMode)
- **Meet Now / Skype** — HideSCAMeetNow registry key
- **OneDrive autostart** — removes Run key + DisableFileSyncNGSC policy
- **Activity Timeline** — EnableActivityFeed + PublishUserActivities
- **Tablet mode** — prevents auto-switch on devices with keyboard attached

---

## 🪟 Part 2 — Windows 11

Targets Windows 11 versions **21H2 through 24H2**, including Copilot+ PCs.

### Menu Options

| Key | Action |
|-----|--------|
| `1` | Install essential apps via Winget |
| `2` | Deep system clean |
| `3` | Debloat using Win11-specific app list (incl. Teams, Clipchamp, Outlook) |
| `4` | Disable background services (opt: keep Xbox) |
| `5` | Gaming Mode — HAGS enabled + Ultimate Performance + VC++ |
| `6` | Privacy Shield — Telemetry, Ads, Start Recommendations |
| `7` | AI Killer — Copilot + Recall + Bing Search |
| `8` | Network Boost — Cloudflare DNS (Win11 method) + TCP tuning |
| `9` | Edge Debloat — AI Sidebar + Startup Boost |
| `A` | Restore classic right-click context menu |
| `B` | Align taskbar left + hide search box |
| `C` | Disable Widgets panel |
| `D` | Kill Teams Chat (taskbar icon + autostart) |
| `E` | Disable Snap Layout suggestions overlay |
| `0` | **Run All** |

### Win11-Exclusive Tweaks
- **Copilot** — TurnOffWindowsCopilot policy + taskbar button hide
- **Recall** — AllowRecallEnablement + DisableAIDataAnalysis (24H2+)
- **Widgets** — AllowNewsAndInterests policy + TaskbarDa key
- **Classic context menu** — CLSID InprocServer32 blank-value trick
- **Taskbar alignment** — TaskbarAl = 0 (left)
- **Snap Layout overlay** — SnapAssist + EnableSnapBar = 0
- **DNS via PowerShell** — uses `Set-DnsClientServerAddress` (Win11 method)

---

## 📥 Installation

```bash
git clone https://github.com/earnerbaymalay/nexus-optimizer
cd nexus-optimizer
pip install -r requirements.txt
```

**Dependencies:** `rich`, `psutil`

---

## 🚀 Usage

> ⚠️ **Must be run as Administrator** (the smart launcher will auto-elevate).

**Option A — Smart Launcher (recommended)**
```bash
python launcher.py
```
Auto-detects Windows version and opens the correct optimizer.

**Option B — Direct**
```bash
# Windows 10:
cd part1_win10 && python main.py

# Windows 11:
cd part2_win11 && python main.py
```

Both scripts prompt to create a **System Restore Point** before any changes are made.

---

## ⚙️ Configuration

| File | Purpose |
|------|---------|
| `part1_win10/config/bloatware_win10.json` | Apps to remove on Win10 (Skype, 3D Viewer, Xbox App…) |
| `part2_win11/config/bloatware_win11.json` | Apps to remove on Win11 (Teams, Clipchamp, Outlook…) |
| `*/config/essential_apps.json` | Apps to install via Winget (Chrome, Steam, VS Code…) |

Edit these JSON files to customise what gets removed or installed.

---

<div align="center">
Made with ❤️ for the Windows community
</div>
