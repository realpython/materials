from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class LinkedList:
    head: Node  # noqa


@dataclass
class Node:
    value: Any
    next: Optional[Node] = None  # noqa
