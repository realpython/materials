from dataclasses import dataclass


@dataclass
class SimplePosition:
    name: str
    lon: float
    lat: float


@dataclass(slots=True)
class SlotPosition:
    name: str
    lon: float
    lat: float
