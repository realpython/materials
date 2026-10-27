from dataclasses import make_dataclass

Position = make_dataclass("Position", ["name", "lon", "lat"])
