from dataclasses import dataclass
from typing import List


@dataclass
class PlayingCard:
    rank: str
    suit: str


@dataclass
class Deck:
    cards: List[PlayingCard]
