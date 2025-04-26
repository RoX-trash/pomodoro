import time
import threading
import pygame

class PomodoroTimer:
    def __init__(self, settings):
        self.settings = settings
        self.work_duration = settings.get("work_duration", 25) * 60
        self.short_break = settings.get("short_break", 5) * 60
        self.pomodoros_until_reset = settings.get("pomodoros_until_reset", 4)
        self.sound_enabled = settings.get("sound_enabled", True)

        self.pomodoro_count = 0
        self.is_running = False
        self.is_break = False
        self.remaining_time = self.work_duration
        self._timer_thread = None
        self._callbacks = []

        pygame.mixer.init()
        self.sound = pygame.mixer.Sound("sound/notify.wav")

    def start(self):
        if not self.is_running:
            self.is_running = True
            self._timer_thread = threading.Thread(target=self._run)
            self._timer_thread.daemon = True
            self._timer_thread.start()

    def pause(self):
        self.is_running = False

    def reset(self):
        self.is_running = False
        self.remaining_time = self.work_duration if not self.is_break else self.short_break

    def skip(self):
        self.is_running = False
        self._switch_phase()

    def on_tick(self, callback):
        self._callbacks.append(callback)

    def _run(self):
        while self.is_running and self.remaining_time > 0:
            time.sleep(1)
            self.remaining_time -= 1
            for callback in self._callbacks:
                callback(self.remaining_time)

        if self.remaining_time == 0:
            self._finish_phase()

    def _finish_phase(self):
        if self.sound_enabled:
            self.sound.play()
        self._switch_phase()

    def _switch_phase(self):
        self.is_break = not self.is_break
        if self.is_break:
            self.remaining_time = self.short_break
        else:
            self.pomodoro_count += 1
            self.remaining_time = self.work_duration
        for callback in self._callbacks:
            callback(self.remaining_time)
