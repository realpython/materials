import numpy as np
from decks import create_high_cards

NUMBER_OF_SUITES = 4
NUMBER_OF_RANKS = 5

high_deck = create_high_cards().reshape((NUMBER_OF_SUITES, NUMBER_OF_RANKS))
rng = np.random.default_rng()

print(rng.permuted(high_deck, axis=0))

print(rng.permuted(high_deck, axis=1))

print(rng.permuted(rng.permuted(high_deck, axis=1), axis=0))
