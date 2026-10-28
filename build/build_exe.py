import subprocess
import sys
import os

def build_exe():
    os.system(f'{sys.executable} -m PyInstaller --onefile --windowed --name "HarmlessVirus" --add-data "app;app" --add-data "core;core" --add-data "models;models" --add-data "utils;utils" app/main.py')

if __name__ == "__main__":
    build_exe()
