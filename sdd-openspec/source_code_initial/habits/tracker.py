from dataclasses import dataclass, field
from datetime import date, timedelta

MAX_BACKDATE_DAYS = 1


@dataclass
class Habit:
    name: str
    check_ins: set[date] = field(default_factory=set)


class Tracker:
    def __init__(self, habits=None):
        self.habits = {habit.name: habit for habit in habits or []}

    def add(self, name):
        name = name.strip().lower()
        if not name:
            raise ValueError("habit name can't be empty")
        if name in self.habits:
            raise ValueError(f"habit '{name}' already exists")
        self.habits[name] = Habit(name)
        return self.habits[name]

    def check_in(self, name, day=None, today=None):
        habit = self._get(name)
        today = today or date.today()
        day = day or today
        if day > today:
            raise ValueError("can't check in on a future date")
        if (today - day).days > MAX_BACKDATE_DAYS:
            raise ValueError("you can only check in for today or yesterday")
        if day in habit.check_ins:
            raise ValueError(f"'{name}' is already checked in for {day}")
        habit.check_ins.add(day)

    def streak(self, name, today=None):
        habit = self._get(name)
        day = today or date.today()
        if day not in habit.check_ins:
            day -= timedelta(days=1)
        count = 0
        while day in habit.check_ins:
            count += 1
            day -= timedelta(days=1)
        return count

    def _get(self, name):
        try:
            return self.habits[name.strip().lower()]
        except KeyError:
            raise KeyError(f"no habit named '{name}'") from None
