from .engine import Engine
from .settings import Settings


def init(settings: Settings) -> None:
    Engine(settings=settings)


def get_engine() -> Engine:
    return Engine()
