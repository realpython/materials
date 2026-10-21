import json
import sys
from datetime import date
from pathlib import Path

DATA_FILE = Path("habits.json")


def load():
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text())
    return {}


def save(data):
    DATA_FILE.write_text(json.dumps(data, indent=2))


def check_in(habit):
    data = load()
    data.setdefault(habit, []).append(date.today().isoformat())
    save(data)


def streak(habit):
    return len(load().get(habit, []))


if __name__ == "__main__":
    command, habit = sys.argv[1], sys.argv[2]
    if command == "done":
        check_in(habit)
    elif command == "streak":
        print(f"{habit}: {streak(habit)} days")
