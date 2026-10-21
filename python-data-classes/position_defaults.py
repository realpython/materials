from dataclasses import dataclass


@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0
