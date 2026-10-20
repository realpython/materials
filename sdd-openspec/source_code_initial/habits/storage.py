import json
from datetime import date
from pathlib import Path

from habits.tracker import Habit, Tracker

DEFAULT_PATH = Path.home() / ".habits.json"


def load(path=DEFAULT_PATH):
    path = Path(path)
    if not path.exists():
        return Tracker()
    data = json.loads(path.read_text(encoding="utf-8"))
    return Tracker(
        Habit(name, {date.fromisoformat(day) for day in days})
        for name, days in data.items()
    )


def save(tracker, path=DEFAULT_PATH):
    data = {
        habit.name: sorted(day.isoformat() for day in habit.check_ins)
        for habit in tracker.habits.values()
    }
    Path(path).write_text(json.dumps(data, indent=2), encoding="utf-8")
