from collections import defaultdict
from smart_quad.core.models import Workout

def accumulate_fatique(history: list[Workout]) -> dict[str, int]:
    fatigue = defaultdict(int)

    for workout in history:
        for muscle, load in workout.muscles.items():
            fatigue[muscle] += load