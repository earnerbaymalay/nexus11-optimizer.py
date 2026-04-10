<div align="center">

# ⚡ N E X U S - O P T I M I Z E R
### *Troubleshooting & Support.*

**[📖 Usage Guide](USAGE.md)** · **[📲 Sideload Hub](https://earnerbaymalay.github.io/sideload/)** · **[↩ Back to README](README.md)**

</div>

---

## Permission Issues

### "Access Denied" errors
- **Must run as Administrator** — right-click PowerShell → "Run as Administrator"
- The smart launcher auto-elevates; accept the UAC prompt
- If UAC is disabled, run manually: `python launcher.py` from an elevated prompt

### System Restore Point fails to create
- Ensure the "Volume Shadow Copy" service is running
- Check available disk space (needs 300MB+ free)
- Run `vssadmin list shadows` to verify VSS is functional

---

## Optimization Issues

### Tweaks don't take effect
- **Restart your computer** after running optimizations
- Some registry changes require a full reboot
- Run `gpupdate /force` to refresh group policies

### Something broke after optimization
- **Restore from System Restore Point** created before changes
- Open `Create a restore point` → System Restore → pick the pre-optimization point
- Or re-run the optimizer and selectively re-enable features

### App won't launch after debloat
- The app may have been in the bloatware list
- Edit the relevant JSON config to remove it from the list
- Reinstall from Microsoft Store or Winget

---

## Network Issues

### Internet stops working after Network Boost
- Cloudflare DNS (1.1.1.1) may not work in all networks
- Reset DNS: `ipconfig /flushdns`
- Or set DNS back to automatic: Network Settings → IPv4 → Automatic

---

## Need More Help?

- **[📖 Read the Usage Guide](USAGE.md)** for full menu documentation.
- **[📲 Visit Sideload Hub](https://earnerbaymalay.github.io/sideload/)** for related projects.
- **[🐛 Report a Bug](https://github.com/earnerbaymalay/nexus11-optimizer.py/issues)** on GitHub.

---

[MIT License](LICENSE)
