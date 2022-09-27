from enum import Enum


class Mood(Enum):
    FUNKY = 1
    MAD = 2
    HAPPY = 3

    def describe_mood(self):
        return self.name, self.value

    def __str__(self):
        return f"I feel {self.name}"

    @classmethod
    def favorite_mood(cls):
        return cls.HAPPY
