from dataclasses import dataclass


@dataclass
class Settings:
    WINDOW_WIDTH: int = 800
    WINDOW_HEIGHT: int = 600
    WINDOW_CAPTION: str = "Hello, Raygine!"
    DESIRED_FPS: int = 60
