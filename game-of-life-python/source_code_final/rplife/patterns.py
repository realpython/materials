from dataclasses import dataclass
from pathlib import Path

try:
    import tomllib as toml
except ImportError:
    import tomli as toml

PATTERNS_FILE = Path(__file__).parent / "patterns.toml"


@dataclass
class Pattern:
    name: str
    alive_cells: set[tuple[int, int]]

    @classmethod
    def from_toml(cls, name, toml_data):
        return cls(
            name,
            alive_cells={tuple(cell) for cell in toml_data["alive_cells"]},
        )


def get_pattern(name, file_name=PATTERNS_FILE):
    data = toml.loads(file_name.read_text(encoding="utf-8"))
    return Pattern.from_toml(name, toml_data=data[name])


def get_all_patterns(file_name=PATTERNS_FILE):
    data = toml.loads(file_name.read_text(encoding="utf-8"))
    return [
        Pattern.from_toml(name, toml_data) for name, toml_data in data.items()
    ]
