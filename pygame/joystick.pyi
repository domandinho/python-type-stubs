from typing import Tuple


def init() -> None:
    ...

def quit() -> None:
    ...


def get_init() -> bool:
    ...


def get_count() -> int:
    ...


class Joystick:
    def __init__(self, id: int) -> None:
        ...

    def init(self) -> None:
        ...

    def quit(self) -> None:
        ...

    def get_init(self) -> bool:
        ...

    def get_id(self) -> int:
        ...

    def get_name(self) -> str:
        ...

    def get_numaxes(self) -> int:
        ...

    def get_axis(self, axis_number: int) -> float:
        ...

    def get_numballs(self) -> int:
        ...

    def get_ball(self, ball_number: int) -> Tuple[float, float]:
        ...

    def get_numbuttons(self) -> int:
        ...

    def get_button(self, button: int) -> bool:
        ...

    def get_numhats(self) -> int:
        ...

    def get_hat(self, hat_number: int) -> Tuple[float, float]:
        ...

