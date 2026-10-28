import sys
import tkinter as tk

def setup_exit(root, key="Escape"):
    def on_exit(event=None):
        root.destroy()
        sys.exit(0)
    root.bind(f"<{key}>", on_exit)
    root.protocol("WM_DELETE_WINDOW", on_exit)
    return on_exit
