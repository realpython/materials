from dataclasses import dataclass, field
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

    def __add__(self, seconds: Numeric | Self) -> Self:
        match seconds:
            case Time() as time:
                return Time(self.seconds + time.seconds)
            case int() | Decimal():
                return Time(self.seconds + seconds)
            case float():
                return Time(self.seconds + Decimal(str(seconds)))
            case Fraction():
                return Time(Fraction.from_decimal(self.seconds) + seconds)
            case _:
                raise TypeError(f"can't add '{type(seconds).__name__}'")

    def __mul__(self, seconds: Numeric) -> Self:
        match seconds:
            case int() | Decimal():
                return Time(self.seconds * seconds)
            case float():
                return Time(self.seconds * Decimal(str(seconds)))
            case Fraction():
                return Time(Fraction.from_decimal(self.seconds) * seconds)
            case _:
                raise TypeError(
                    f"can't multiply by '{type(seconds).__name__}'"
                )

    def get_num_samples(self, sampling_rate: Hertz) -> int:
        return round(self.seconds * round(sampling_rate))


@dataclass
class Timeline:
    instant: Time = Time(seconds=0)

    def __rshift__(self, seconds: Numeric | Time) -> Self:
        self.instant += seconds
        return self


@dataclass
class MeasuredTimeline(Timeline):
    measure: Time = Time(seconds=0)
    last_measure_ended_at: Time = field(init=False, repr=False)

    def __post_init__(self) -> None:
        if self.measure.seconds > 0 and self.instant.seconds > 0:
            periods = self.instant.seconds // self.measure.seconds
            self.last_measure_ended_at = Time(periods * self.measure.seconds)
        else:
            self.last_measure_ended_at = Time(seconds=0)

    def __next__(self) -> Self:
        if self.measure.seconds <= 0:
            raise ValueError("measure duration must be positive")
        self.last_measure_ended_at += self.measure
        self.instant = self.last_measure_ended_at
        return self
