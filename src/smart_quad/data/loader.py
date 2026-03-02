from __future__ import annotations

from importlib import resources

import yaml
from smart_quad.core.models import Workout
from smart_quad.core.constants import MAX_MUSCLE_LOAD, VALID_MUSCLES

from typing import Any

def _read_package_yaml(filename: str) -> Any:
    """
    Reads a YAML file that lives inside the installed package.

    Why this approach?
    - Works the same in PyCharm, terminal, CI
    - No fragile relative paths like "src/..."
    """
    package = "smart_quad.data"
    yaml_path = resources.files(package).joinpath(filename)
    with yaml_path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_workouts(path: str) -> list[Workout]:
    raw = _read_package_yaml("workouts.yaml")

    if not isinstance(raw, dict):
        raise ValueError("workouts.yaml: root must be a mapping (dict)")

    if "workouts" not in raw:
        raise ValueError("workouts.yaml: missing top-level key 'workouts'")

    workouts_raw = raw["workouts"]
    if not isinstance(workouts_raw, list):
        raise ValueError("workouts.yaml: 'workouts' must be a list")
    workouts: list[Workout] = []

    for idx, entry in enumerate(workouts_raw, start=1):
        if not isinstance(entry, dict):
            raise ValueError(f"workouts.yaml: workout #{idx} must be a mapping")

        name = entry.get("name")
        muscles = entry.get("muscles")

        if not isinstance(name, str) or not name.strip():
            raise ValueError(f"workouts.yaml: workout #{idx} has invalid name")

        if not isinstance(muscles, dict):
            raise ValueError(f"workouts.yaml: workout '{name}' has invalid 'muscles'")

        validated: dict[str, int] = {}
        for muscle, load in muscles.items():
            if muscle not in VALID_MUSCLES:
                raise ValueError(f"workouts.yaml: workout '{name}' unknown muscle '{muscle}'")
            if not isinstance(load, int): raise ValueError(
                f"workouts.yaml: workout '{name}' load for '{muscle}' must be int")
            if not 0 <= load <= MAX_MUSCLE_LOAD: raise ValueError(
                f"workouts.yaml: workout '{name}' load for '{muscle}' must be in 0..{MAX_MUSCLE_LOAD}")
            validated[muscle] = load
        workouts.append(Workout(name=name, muscles=validated))


    return workouts
