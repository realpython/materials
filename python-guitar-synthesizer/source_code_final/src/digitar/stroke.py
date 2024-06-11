import enum
from dataclasses import dataclass
from typing import Self

from digitar.temporal import Time


class Direction(enum.Enum):
    DOWN = enum.auto()
    UP = enum.auto()


@dataclass(frozen=True)
class Velocity:
    direction: Direction
    delay: Time

    @classmethod
    def down(cls, delay: Time) -> Self:
        return cls(Direction.DOWN, delay)

    @classmethod
    def up(cls, delay: Time) -> Self:
        return cls(Direction.UP, delay)
