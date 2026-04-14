from collections import defaultdict
from smart_quad.core.models import Workout


def compute_fatigue(history: list[Workout]) -> dict[str, float]:
    """
    Accumulates fatigue from workout history.

    Think of fatigue like "water in buckets" per muscle:
    - each workout pours water into some buckets
    - the more you train a muscle, the fuller its bucket gets
    """

    fatigue: defaultdict[str, float] = defaultdict(float)
    for workout in history:
        for muscle, load in workout.muscles.items():
            fatigue[muscle] += float(load)

    return dict(fatigue)



def apply_recovery(fatigue: dict[str, float], recovery_rate: float) -> dict[str, float]:
    """
    Applies recovery by reducing fatigue.

    recovery_rate is a fraction in [0, 1]:
    - 0.35 means: reduce fatigue by 35% each run/day-step

    This is a simple exponential decay model:
        new = old * (1 - recovery_rate)

    Why this model?
    - stable
    - easy to reason about
    - common in many systems (cooling, depreciation, forgetting curves)
    """

    if not 0.0 <= recovery_rate <= 1.0:
        raise ValueError("recovery_rate must be in [0, 1]")

    recovered: dict[str, float] = {}
    for muscle, value in fatigue.items():
        new_value = value * (1.0 - recovery_rate)

        #clamp tiny values to 0 to avoid endless decimals
        recovered[muscle] = 0.0 if new_value < 0.01 else new_value

    return recovered
