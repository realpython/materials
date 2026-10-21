from datetime import date

from habits import storage
from habits.tracker import Tracker


def test_round_trip(tmp_path):
    path = tmp_path / "habits.json"
    tracker = Tracker()
    tracker.add("read")
    tracker.check_in("read", date(2026, 10, 11), today=date(2026, 10, 12))
    storage.save(tracker, path)

    loaded = storage.load(path)
    assert loaded.habits["read"].check_ins == {date(2026, 10, 11)}


def test_missing_file_gives_empty_tracker(tmp_path):
    assert storage.load(tmp_path / "nope.json").habits == {}
