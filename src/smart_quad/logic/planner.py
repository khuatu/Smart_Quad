from smart_quad.core.models import Workout

def choose_next(workouts: list[Workout], fatigue: dict[str, int]) -> Workout:
    return min(
        workouts,
        key = lambda w: sum(fatigue.get(m, 0) for m in w.muscles)
    )