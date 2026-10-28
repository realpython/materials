from dataclasses import dataclass
from typing import Any


@dataclass
class WithoutExplicitTypes:
    name: Any
    value: Any = 42
