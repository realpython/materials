from dataclasses import dataclass


@dataclass
class Position:
    name: str
    lon: float
    lat: float


@dataclass
class Capital(Position):
    country: str
