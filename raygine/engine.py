import atexit
from typing import NoReturn
import sys
import raylibpy as rp
from .settings import Settings


class Engine:
    def __init__(self, settings: Settings) -> None:
        self._settings: Settings = settings
        rp.init_window(settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT, settings.WINDOW_CAPTION)
        # rp.init_audio_device()
        rp.set_target_fps(settings.DESIRED_FPS)
    
    def run(self) -> None:
        while not rp.window_should_close():
            rp.begin_drawing()
            rp.clear_background(rp.RAYWHITE)
            rp.end_drawing()

    @staticmethod
    @atexit.register
    def exit() -> NoReturn:
        # rp.close_audio_device()
        rp.close_window()