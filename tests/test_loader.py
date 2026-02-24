def test_load_workouts():
    workouts = load_workouts("tests/data/sample_workouts.yaml")
    assert len(workouts) == 2
