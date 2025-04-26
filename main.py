import customtkinter as ctk
import json
import os
from timer import PomodoroTimer
from ui import PomodoroUI

CONFIG_PATH = os.path.join("settings.json")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Pomospike")
        self.geometry("480x320")
        self.resizable(False, False)
        self.configure(fg_color="#121212")

        self.settings = self.load_settings()
        self.timer = PomodoroTimer(self.settings)
        self.ui = PomodoroUI(self, self.timer)

        self.ui.pack(expand=True, fill="both")

    def load_settings(self):
        if not os.path.exists(CONFIG_PATH):
            return {
                "work_duration": 25,
                "short_break": 5,
                "pomodoros_until_reset": 4,
                "sound_enabled": True
            }
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)

if __name__ == "__main__":
    app = App()
    app.mainloop()
