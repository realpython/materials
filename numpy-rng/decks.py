import numpy as np


def create_deck():
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
    SUITS = "♣ ♢ ♡ ♠".split()
    return np.array([r + s for s in SUITS for r in RANKS])


def create_high_cards():
    HIGH_CARDS = "10 J Q K A".split()
    SUITS = "♣ ♢ ♡ ♠".split()
    return np.array([r + s for s in SUITS for r in HIGH_CARDS])


if __name__ == "__main__":
    print("Full deck:\n", create_deck(), end="\n\n")
    print("High cards:\n", create_high_cards(), end="\n\n")
