from fractions import Fraction
from functools import cached_property
from pathlib import Path
from typing import Optional, Self

import yaml
from pydantic import (
    BaseModel,
    HttpUrl,
    NonNegativeFloat,
    NonNegativeInt,
    PositiveFloat,
    PositiveInt,
    confloat,
    conlist,
    constr,
    model_validator,
)

DEFAULT_STRING_DAMPING: float = 0.5
DEFAULT_ARPEGGIO_SECONDS: float = 0.005


class Note(BaseModel):
    frets: conlist(NonNegativeInt | None, min_length=1)
    offset: Optional[constr(pattern=r"\d+/\d+")] = "0/1"
    upstroke: Optional[bool] = False
    arpeggio: Optional[NonNegativeFloat] = DEFAULT_ARPEGGIO_SECONDS
    vibration: Optional[PositiveFloat] = None


class Measure(BaseModel):
    time_signature: constr(pattern=r"\d+/\d+")
    notes: Optional[tuple[Note, ...]] = tuple()

    @cached_property
    def beats_per_measure(self) -> int:
        return int(self.time_signature.split("/")[0])

    @cached_property
    def note_value(self) -> Fraction:
        return Fraction(1, int(self.time_signature.split("/")[1]))


class Tablature(BaseModel):
    beats_per_minute: PositiveInt
    measures: tuple[Measure, ...]


class Instrument(BaseModel):
    tuning: conlist(constr(pattern=r"([A-G]#?)(-?\d+)?"), min_length=1)
    vibration: PositiveFloat
    damping: Optional[confloat(ge=0, le=0.5)] = DEFAULT_STRING_DAMPING
    effects: Optional[tuple[str | dict, ...]] = tuple()


class Track(BaseModel):
    url: Optional[HttpUrl] = None
    weight: Optional[NonNegativeFloat] = 1.0
    instrument: Instrument
    tablature: Tablature

    @model_validator(mode="after")
    def check_frets(self) -> Self:
        num_strings = len(self.instrument.tuning)
        for measure in self.tablature.measures:
            for notes in measure.notes:
                if len(notes.frets) != num_strings:
                    raise ValueError("Incorrect number of frets")
        return self


class Song(BaseModel):
    title: Optional[str] = None
    artist: Optional[str] = None
    tracks: dict[str, Track]

    @classmethod
    def from_file(cls, path: str | Path) -> Self:
        with Path(path).open(encoding="utf-8") as file:
            return cls(**yaml.safe_load(file))
