import tkinter as tk
import random
import time
from app.config import *
from core.renderer import Renderer
from core.screen import ScreenManager
from models.text_data import LOG_LINES, WARNING_POPUPS
from utils.exit_handler import setup_exit

class Engine:
    def __init__(self):
        self.root = tk.Tk()
        self.screen = ScreenManager(self.root)
        self.canvas = self.screen.create_canvas()
        self.renderer = Renderer(self.root, self.canvas)
        self.line_idx = 0
        self.running = True
        setup_exit(self.root, EXIT_KEY)
        self.countdown_label = None

    def next_line(self):
        if not self.running:
            return
        line = LOG_LINES[self.line_idx % len(LOG_LINES)]
        self.renderer.add_line(line)
        self.line_idx += 1
        if random.random() < SHAKE_CHANCE:
            self.renderer.shake()
        if random.random() < 0.05:
            self.renderer.flash_screen()
        self.root.after(SCROLL_SPEED_MS, self.next_line)

    def popup_loop(self):
        if not self.running:
            return
        msg = random.choice(WARNING_POPUPS)
        self.screen.show_popup(msg)
        delay = random.randint(POPUP_INTERVAL_MIN, POPUP_INTERVAL_MAX)
        self.root.after(delay, self.popup_loop)

    def countdown_timer(self):
        seconds = 86400
        def tick():
            nonlocal seconds
            if not self.running:
                return
            m, s = divmod(seconds, 60)
            h, m = divmod(m, 60)
            time_str = f"TIME REMAINING: {h:02d}:{m:02d}:{s:02d}"
            if self.countdown_label:
                self.canvas.itemconfig(self.countdown_label, text=time_str)
            else:
                self.countdown_label = self.canvas.create_text(
                    WIDTH//2, HEIGHT-40, text=time_str,
                    fill=TEXT_COLOR_RED, font=(FONT_FAMILY, 20, "bold")
                )
            seconds -= 1
            if seconds < 0:
                seconds = 86400
            self.root.after(1000, tick)
        tick()

    def run(self):
        self.next_line()
        self.popup_loop()
        self.countdown_timer()
        self.root.mainloop()
