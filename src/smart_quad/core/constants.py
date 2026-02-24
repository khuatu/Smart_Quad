from __future__ import annotations

from typing import Final

MAX_MUSCLE_LOAD: Final[int] = 10

VALID_MUSCLES: Final[set[str]] = {
    "chest",
    "shoulders",
    "lats",
    "biceps",
    "triceps",
    "core",
    "quadriceps",
    "hamstrings",
    "glutes",
    "calves",
}

HISTORY_JSON_NAME: Final[str] = "training_history.json"


