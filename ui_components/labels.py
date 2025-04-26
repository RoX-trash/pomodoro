import customtkinter as ctk

class TimerLable(ctk.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(
            master=master,
            text='25:00',
            font = ctk.CTkFont(size=48, weight='bold'),
            text_color = '#FFFFFF',
            **kwargs
        )
class ModeLable(ctk.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(
            master=master,
            text='Работа',
            font=ctk.CTkFont(size=18),
            text_color='#FFFFFF',
            **kwargs
        )


