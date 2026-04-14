from __future__ import annotations

from smart_quad.core.models import Workout


def choose_next_workout(workouts: list[Workout], fatigue: dict[str, float]) -> Workout:
    """
    Chooses the next workout by minimizing overlap with currently fatigued muscles.

    Intuition:
    - If legs are very fatigued, avoid workouts that heavily load legs.
    - If upper body is fatigued, choose legs, etc.

    We compute a "fatigue cost" for each workout:
        cost(workout) = sum( fatigue[muscle] * load(workout, muscle) )

    Why multiply?
    - If a muscle is fatigued AND the workout loads it strongly, that's bad.
    - If a muscle is fatigued but the workout doesn't use it, no penalty.
    - If a muscle is fresh, penalty stays low.

    This is a simple, explainable planner.
    Later you can add:
    - minimum frequency constraints
    - goals (prioritize weak muscles)
    - user preferences
    - randomness with seed
    """
    if not workouts:
        raise ValueError("No workouts available to plan from")

    def cost(w: Workout) -> float:
        total = 0.0
        for muscle, load in w.muscles.items():
            total += fatigue.get(muscle, 0.0) * float(load)
        return total

    # Deterministic: always picks the lowest cost.
    # Tie-breaker: if costs equal, pick the one with lower total load, then name.
    return min(
        workouts,
        key=lambda w: (cost(w), w.total_load(), w.name.lower()),
    )
