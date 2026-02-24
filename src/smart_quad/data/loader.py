import yaml
from smart_quad.core.models import Workout
from smart_quad.core.constants import MAX_MUSCLE_LOAD, VALID_MUSCLES

def load_workouts(path: str) -> list[Workout]:
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    workouts = []
    for w in data["workouts"]:
        muscles = w["muscles"]

        for m, load in muscles.items():
            if m not in VALID_MUSCLES:
                raise ValueError(f"Unknown muscle: {m}")
            if not (0 <= load <= MAX_MUSCLE_LOAD):
                raise ValueError(f"Invalid load {load} for {m}")

        workouts.append(Workout(name=w["name"], muscles=muscles))

    return workouts
