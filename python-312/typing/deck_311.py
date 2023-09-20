import random
from typing import TypeAlias

CardDeck: TypeAlias = list[tuple[str, int]]


def shuffle(deck: CardDeck) -> CardDeck:
    return random.sample(deck, k=len(deck))
