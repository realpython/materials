import numpy as np
from decks import create_deck

rng = np.random.default_rng()
deck_of_cards = create_deck()

rng.shuffle(deck_of_cards)
print(deck_of_cards[0:3])

rng.shuffle(deck_of_cards)
print(deck_of_cards[0:3])
