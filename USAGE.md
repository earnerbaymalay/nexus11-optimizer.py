<div align="center">

# ⚡ N E X U S - O P T I M I Z E R
### *Usage Guide & Instructions.*

**[🔧 Troubleshooting](TROUBLESHOOTING.md)** · **[📲 Sideload Hub](https://earnerbaymalay.github.io/sideload/)** · **[↩ Back to README](README.md)**

</div>

---

## Installation

```bash
git clone https://github.com/earnerbaymalay/nexus11-optimizer.py.git
cd nexus11-optimizer.py
pip install -r requirements.txt
```

**Dependencies:** `rich`, `psutil`

---

## Running the Optimizer

### Smart Launcher (Recommended)

```bash
python launcher.py
```

Auto-detects Windows version (10 or 11) and opens the correct optimizer.

### Direct Launch

```bash
# Windows 10:
cd part1_win10 && python main.py

# Windows 11:
cd part2_win11 && python main.py
```

> ⚠️ **Must run as Administrator.** The smart launcher will auto-elevate.

---

## Menu Options

### Windows 10 Menu

| Key | Action |
|-----|--------|
| `1` | Install essential apps via Winget |
| `2` | Deep system clean (Temp, WinSxS, Logs) |
| `3` | Debloat (Win10-specific app list) |
| `4` | Disable background services |
| `5` | Gaming Mode — Ultimate Performance + VC++ |
| `6` | Privacy Shield — Telemetry, Ads, Activity History |
| `7` | Cortana & AI Killer |
| `8` | Network Boost — Cloudflare DNS + TCP tuning |
| `9` | Edge Debloat |
| `A` | Win10 UI Tweaks |
| `B` | Kill News & Interests widget |
| `C` | Disable OneDrive autostart + Remove Meet Now |
| `0` | **Run All** |

### Windows 11 Menu

| Key | Action |
|-----|--------|
| `1`-`6` | Same as Win10 |
| `7` | AI Killer — Copilot + Recall + Bing Search |
| `8` | Network Boost (Win11 method) |
| `9` | Edge Debloat — AI Sidebar + Startup Boost |
| `A` | Restore classic right-click context menu |
| `B` | Align taskbar left + hide search box |
| `C` | Disable Widgets panel |
| `D` | Kill Teams Chat |
| `E` | Disable Snap Layout suggestions |
| `0` | **Run All** |

---

## Configuration

Edit JSON files to customize what gets removed or installed:

| File | Purpose |
|------|---------|
| `part1_win10/config/bloatware_win10.json` | Apps to remove on Win10 |
| `part2_win11/config/bloatware_win11.json` | Apps to remove on Win11 |
| `*/config/essential_apps.json` | Apps to install via Winget |

---

## Safety

- A **System Restore Point** is created before any changes
- Each tweak is logged for auditability
- Individual options can be run without "Run All"

---

## Troubleshooting

See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for common issues.

---

[MIT License](LICENSE)
