from enum import Enum


class WeekDay(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    @classmethod
    def favorite_day(cls):
        return cls.FRIDAY

    def __str__(self):
        return f"Current day: {self.name}"
