from .constants import SECS_PER_HOUR as SECS_PER_HOUR, SECS_PER_MIN as SECS_PER_MIN, USECS_PER_SEC as USECS_PER_SEC
from .duration import AbsoluteDuration as AbsoluteDuration, Duration as Duration
from .mixins.default import FormattableMixin as FormattableMixin
from datetime import time
from typing import Any, Optional

class Time(FormattableMixin, time):
    def closest(self, dt1: Any, dt2: Any): ...
    def farthest(self, dt1: Any, dt2: Any): ...
    def add(self, hours: int = ..., minutes: int = ..., seconds: int = ..., microseconds: int = ...): ...
    def subtract(self, hours: int = ..., minutes: int = ..., seconds: int = ..., microseconds: int = ...): ...
    def add_timedelta(self, delta: Any): ...
    def subtract_timedelta(self, delta: Any): ...
    def __add__(self, other: Any): ...
    def __sub__(self, other: Any): ...
    def __rsub__(self, other: Any): ...
    def diff(self, dt: Optional[Any] = ..., abs: bool = ...): ...
    def diff_for_humans(self, other: Optional[Any] = ..., absolute: bool = ..., locale: Optional[Any] = ...): ...
    def replace(self, hour: Optional[Any] = ..., minute: Optional[Any] = ..., second: Optional[Any] = ..., microsecond: Optional[Any] = ..., tzinfo: bool = ...): ...
    def __getnewargs__(self): ...
    def __reduce__(self): ...
    def __reduce_ex__(self, protocol: Any): ...