from smart_quad.core.models import Workout

def score_workout(workout: Workout) -> int:
    """
    Calculating total load of a workout
    """

    return workout.total_load()