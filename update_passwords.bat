@echo off
cd /d "%~dp0"
venv\Scripts\python.exe update_passwords.py
pause


