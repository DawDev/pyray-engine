from dataclasses import dataclass
from typing import Literal


class Entity:
    def __init__(self) -> None:
        self._render_type: Literal["rectangle"] = "rectangle"
        self._name: str = "Unknown"
        self._position: tuple[int, int] = (0, 0)
        self._color: tuple[int, int, int] = (255, 255, 255)
        self._rectangle: tuple[int, int, int, int] = (0, 0, 0, 0)

    def update_rect(self) -> None:
        self._rectangle[0] = self._position[0]
        self._rectangle[1] = self._position[1]

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def position(self) -> tuple[int, int]:
        return self._position

    @position.setter
    def position(self, value: tuple[int, int]):
        self._position = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value: tuple[int, int, int]) -> tuple[int, int, int]:
        self._color = value

    def update(self) -> None: ...

    def render(self) -> None: ...

    def load(self) -> None: ...

    def unload(self) -> None: ...