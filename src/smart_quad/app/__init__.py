from __future__ import annotations

from smart_quad.data.loader import load_workouts
from smart_quad.data.history import load_history,append_to_history
from smart_quad.logic.recovery import compute_fatigue, apply_recovery
from smart_quad.logic.planner import choose_next_workout
from smart_quad.logic.scoring import score_workout

def run() -> None:
    """
    Orchestriert den Ablauf der Anwendung:
    - lädt Workouts (YAML)
    - lädt Historie (JSON)
    - berechnet Fatigue + Recovery
    - plant nächstes Workout
    - speichert Entscheidung
    - gibt Ergebnis aus
    """

    workouts = load_workouts()
    history = load_history()

    fatigue = compute_fatigue(history)
    fatigue = apply_recovery(fatigue, recovery_rate=0.35)

    next_workout = choose_next_workout(workouts, fatigue)
    score = score_workout(next_workout)

    append_to_history(next_workout)

    print("=" * 72)
    print("Smart_Quad")
    print("=" * 72)
    print(f"Loaded workouts: {len(workouts)}")
    print(f"History entries: {len(history)}")
    print("-" * 72)
    print("Current fatigue (after recovery):")
    if not fatigue:
        print(" (no fatigue yet)")
    else:
        for muscle, value in sorted(fatigue.items()):
            print(f" {muscle:12s}: {value:.2f}")
    print("-" * 72)
    print("Next workout suggestion:")
    print(f" name: {next_workout.name}")
    print(f" score: {score}")
    print(" muscles:")
    for muscle, load in next_workout.muscles.items():
        print(f" {muscle:12s}: {load}")
    print("=" * 72)

