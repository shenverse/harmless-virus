import tkinter as tk
import random
from app.config import *

class Renderer:
    def __init__(self, root, canvas):
        self.root = root
        self.canvas = canvas
        self.y_pos = 50
        self.lines_shown = []

    def add_line(self, text, color=None):
        if color is None:
            color = TEXT_COLOR_GREEN
            if text.startswith("[!]"):
                color = TEXT_COLOR_RED
        line = self.canvas.create_text(
            50, self.y_pos, anchor="w", text=text,
            fill=color, font=(FONT_FAMILY, FONT_SIZE)
        )
        self.lines_shown.append(line)
        self.y_pos += 24
        if self.y_pos > HEIGHT - 100:
            self.clear_old()

    def clear_old(self):
        if len(self.lines_shown) > 30:
            old = self.lines_shown.pop(0)
            self.canvas.delete(old)
            self.canvas.move("all", 0, -24)
            self.y_pos -= 24

    def flash_screen(self):
        self.canvas.configure(bg=TEXT_COLOR_RED)
        self.root.after(50, lambda: self.canvas.configure(bg=BG_COLOR))

    def shake(self):
        dx = random.randint(-SHAKE_INTENSITY, SHAKE_INTENSITY)
        dy = random.randint(-SHAKE_INTENSITY, SHAKE_INTENSITY)
        self.root.geometry(f"+{dx}+{dy}")
        self.root.after(100, lambda: self.root.geometry("+0+0"))
