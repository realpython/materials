from typing import Self


class Chord(tuple[int | None, ...]):
    @classmethod
    def from_numbers(cls, *numbers: int | None) -> Self:
        return cls(numbers)
