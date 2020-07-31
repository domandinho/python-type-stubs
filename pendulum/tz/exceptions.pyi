from typing import Any

class TimezoneError(ValueError): ...

class NonExistingTime(TimezoneError):
    message: str = ...
    def __init__(self, dt: Any) -> None: ...

class AmbiguousTime(TimezoneError):
    message: str = ...
    def __init__(self, dt: Any) -> None: ...