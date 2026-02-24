from dataclasses import dataclass
from typing import Dict

@dataclass(frozen=True)
class Workout:
    name: str
    muscles: Dict[str, int]