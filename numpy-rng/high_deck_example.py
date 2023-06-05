from decks import create_high_cards

NUMBER_OF_SUITES = 4
NUMBER_OF_RANKS = 5

high_deck = create_high_cards().reshape((NUMBER_OF_SUITES, NUMBER_OF_RANKS))
print(high_deck)
