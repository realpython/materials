import numpy as np
from decks import create_high_cards

NUMBER_OF_SUITES = 4
NUMBER_OF_RANKS = 5

rng = np.random.default_rng()

high_deck = create_high_cards().reshape((NUMBER_OF_SUITES, NUMBER_OF_RANKS))
print(rng.permutation(high_deck, axis=0))
print(rng.permutation(high_deck, axis=0))

print(rng.permutation(high_deck, axis=1))
print(rng.permutation(high_deck, axis=1))

print(high_deck)

rng.shuffle(high_deck, axis=0)
print(high_deck)
rng.shuffle(high_deck, axis=1)
print(high_deck)
