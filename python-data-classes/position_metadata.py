from dataclasses import dataclass, field


@dataclass
class Position:
    name: str
    lon: float = field(default=0.0, metadata={"unit": "degrees"})
    lat: float = field(default=0.0, metadata={"unit": "degrees"})
