from dataclasses import dataclass
from decimal import Decimal
from fractions import Fraction
from typing import Self

type Numeric = int | float | Decimal | Fraction
type Hertz = int | float


@dataclass(frozen=True)
class Time:
    seconds: Decimal

    @classmethod
    def from_milliseconds(cls, milliseconds: Numeric) -> Self:
        return cls(Decimal(str(float(milliseconds))) / 1000)

    def __init__(self, seconds: Numeric) -> None:
        match seconds:
            case int() | float():
                object.__setattr__(self, "seconds", Decimal(str(seconds)))
            case Decimal():
                object.__setattr__(self, "seconds", seconds)
            case Fraction():
                object.__setattr__(
                    self, "seconds", Decimal(str(float(seconds)))
                )
            case _:
                raise TypeError(f"unsupported type '{type(seconds).__name__}'")

    def get_num_samples(self, sampling_rate: Hertz) -> int:
        return round(self.seconds * round(sampling_rate))
