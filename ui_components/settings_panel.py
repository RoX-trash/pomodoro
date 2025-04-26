import customtkinter as ctk

class SettingsPanel(ctk.CTkFrame):
    def __init__(self, master, timer, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        self.timer = timer

        self.label_work = ctk.CTkLabel(self, text="Работа (мин):", text_color="#ffffff")
        self.entry_work = ctk.CTkEntry(self, width=50)
        self.entry_work.insert(0, str(self.timer.settings["work_duration"]))

        self.label_break = ctk.CTkLabel(self, text="Отдых (мин):", text_color="#ffffff")
        self.entry_break = ctk.CTkEntry(self, width=50)
        self.entry_break.insert(0, str(self.timer.settings["short_break"]))

        self.sound_checkbox = ctk.CTkCheckBox(self, text="Звук", text_color="#ffffff")
        self.sound_checkbox.select() if self.timer.settings["sound_enabled"] else self.sound_checkbox.deselect()

        self.apply_button = ctk.CTkButton(self, text="Применить", command=self.apply_settings, corner_radius=8)

        self.label_work.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_work.grid(row=0, column=1, padx=5, pady=5)
        self.label_break.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_break.grid(row=1, column=1, padx=5, pady=5)
        self.sound_checkbox.grid(row=2, column=0, columnspan=2, pady=(10, 5))
        self.apply_button.grid(row=3, column=0, columnspan=2, pady=10)

    def apply_settings(self):
        try:
            work = int(self.entry_work.get())
            rest = int(self.entry_break.get())
            sound = self.sound_checkbox.get()

            self.timer.update_settings({
                "work_duration": work,
                "short_break": rest,
                "sound_enabled": sound
            })
        except ValueError:
            print("Ошибка: Введите корректные числовые значения.")
