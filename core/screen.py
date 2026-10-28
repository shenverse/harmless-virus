import tkinter as tk
from app.config import *

class ScreenManager:
    def __init__(self, root):
        self.root = root
        self.setup_fullscreen()

    def setup_fullscreen(self):
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg=BG_COLOR)
        self.root.title(TITLE)
        self.root.attributes("-topmost", True)

    def create_canvas(self):
        canvas = tk.Canvas(
            self.root, bg=BG_COLOR, highlightthickness=0
        )
        canvas.pack(fill="both", expand=True)
        return canvas

    def show_popup(self, message):
        popup = tk.Toplevel(self.root)
        popup.title("WARNING")
        popup.configure(bg="#1a1a1a")
        popup.geometry("400x200")
        popup.attributes("-topmost", True)
        x = random.randint(200, 1200)
        y = random.randint(150, 600)
        popup.geometry(f"+{x}+{y}")
        label = tk.Label(
            popup, text=message, bg="#1a1a1a", fg=TEXT_COLOR_RED,
            font=(FONT_FAMILY, 11), justify="left", padx=20, pady=20
        )
        label.pack()
        btn = tk.Button(
            popup, text="OK", command=popup.destroy,
            bg=TEXT_COLOR_RED, fg=TEXT_COLOR_WHITE,
            font=(FONT_FAMILY, 10), width=10
        )
        btn.pack(pady=10)
        popup.after(4000, popup.destroy)
