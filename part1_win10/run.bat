@echo off
:: NEXUS OPTIMIZER — Part 1: Windows 10
:: Double-click to launch (auto-elevates to Administrator)
cd /d "%~dp0"
powershell -Command "Start-Process python -ArgumentList 'main.py' -Verb RunAs -WorkingDirectory '%~dp0'"
