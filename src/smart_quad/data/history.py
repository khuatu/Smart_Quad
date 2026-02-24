import json
from smart_quad.core.models import Workout

HISTORY_FILE = "training_history.json"

def save_history(history: list[Workout]) -> None:
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(
            [{"name": w.name, "muscles": w.muscles} for w in history],
            f,
            indent=2
    )

