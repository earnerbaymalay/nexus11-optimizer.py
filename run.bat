@echo off
:: NEXUS OPTIMIZER — Smart Launcher
:: Auto-detects Windows version and opens the correct optimizer
cd /d "%~dp0"
powershell -Command "Start-Process python -ArgumentList 'launcher.py' -Verb RunAs -WorkingDirectory '%~dp0'"
