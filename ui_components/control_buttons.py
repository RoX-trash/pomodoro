import customtkinter as ctk
from ui_components.labels import TimerLabel, ModeLabel

class TimerDisplay(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.mode_label = ModeLabel(self)
        self.mode_label.pack(pady=(10, 0))

        self.timer_label = TimerLabel(self)
        self.timer_label.pack(pady=(0, 10))

    def update_timer(self, time_text):
        self.timer_label.configure(text=time_text)

    def update_mode(self, mode_text):
        self.mode_label.configure(text=mode_text)
