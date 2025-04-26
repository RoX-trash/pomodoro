import customtkinter as ctk
from ui_components.timer_display import TimerDisplay
from ui_components.control_buttons import ControlButtons
from ui_components.settings_panel import SettingsPanel

class PomodoroUI(ctk.CTkFrame):
    def __init__(self, master, timer):
        super().__init__(master)
        self.timer = timer

        self.configure(fg_color="#121212")

        self.timer_display = TimerDisplay(self, timer)
        self.control_buttons = ControlButtons(self, timer)
        self.settings_panel = SettingsPanel(self, timer)

        self.timer_display.pack(pady=(20, 10))
        self.control_buttons.pack(pady=(0, 10))
        self.settings_panel.pack(pady=(0, 20))
