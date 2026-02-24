from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class Workout:
    """
    Immutable domain object.

    'frozen=True' means: once created, it cannot be changed.
    This prevents accidental side effects across your system.
    """
    name: str
    muscles: Mapping[str, int]

    def total_load(self) -> int:
        return sum(self.muscles.values())

    def load_for(self, muscle: str) -> int:
        return self.muscles.get(muscle, 0)
