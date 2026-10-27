# Data Classes in Python (Guide)

This folder provides the code examples for the Real Python tutorial [Data Classes in Python (Guide)](https://realpython.com/python-data-classes/).

## Installation

Most examples only use the standard library. To run the `attrs` example and the memory measurements with Pympler, install the third-party packages into a virtual environment:

```sh
$ python -m pip install -r requirements.txt
```

The code requires Python 3.10 or later because `slots.py` uses `@dataclass(slots=True)`. All other data class examples run on Python 3.7 or later, and `attrs_card.py` needs Python 3.9 or later for `attrs` 26.1.

## Files

### Data Class Alternatives

- `data_class_card.py`: A minimal `DataClassCard` data class
- `regular_card_v1.py`: A minimal `RegularCard` regular class, without a nice representation or equality
- `regular_card_v2.py`: `RegularCard` with hand-written `.__repr__()` and `.__eq__()` methods
- `named_tuple_card.py`: `NamedTupleCard` built with `collections.namedtuple`
- `attrs_card.py`: `AttrsCard` built with the third-party `attrs` package

```pycon
>>> from data_class_card import DataClassCard
>>> queen_of_hearts = DataClassCard("Q", "Hearts")
>>> queen_of_hearts
DataClassCard(rank='Q', suit='Hearts')
>>> queen_of_hearts == DataClassCard("Q", "Hearts")
True
```

### Basic Data Classes

- `position.py`: A basic `Position` data class with `name`, `lon`, and `lat` fields
- `position_make_dataclass.py`: `Position` created with `make_dataclass()`
- `position_defaults.py`: `Position` with default values
- `without_explicit_types.py`: A data class using `typing.Any` instead of explicit types
- `position_distance.py`: `Position` with a `.distance_to()` method using the haversine formula

```pycon
>>> from position_distance import Position
>>> oslo = Position("Oslo", 10.8, 59.9)
>>> vancouver = Position("Vancouver", -123.1, 49.3)
>>> oslo.distance_to(vancouver)
7181.7841229421165
```

### More Flexible Data Classes

- `deck_v1.py`: `PlayingCard` and a `Deck` holding a list of cards
- `deck_v2.py`: Adds `RANKS`, `SUITS`, `make_french_deck()`, and a `default_factory` for `Deck`
- `position_metadata.py`: `Position` with field metadata set through `field()`
- `deck_v3.py`: Adds a `.__str__()` method to `PlayingCard` and a concise `.__repr__()` to `Deck`
- `deck_v4.py`: Makes `PlayingCard` orderable with `order=True`, which compares cards alphabetically
- `deck_v5.py`: Adds a `.sort_index` computed in `.__post_init__()` so cards compare in the right order

```pycon
>>> from deck_v5 import Deck, PlayingCard, make_french_deck
>>> PlayingCard("A", "♠") > PlayingCard("Q", "♡")
True
>>> Deck(sorted(make_french_deck()))
Deck(♣2, ♢2, ♡2, ♠2, ♣3, ♢3, ♡3, ♠3, ♣4, ♢4, ♡4, ♠4, ♣5, ♢5, ♡5, ♠5, ♣6, ♢6, ♡6, ♠6, ♣7, ♢7, ♡7, ♠7, ♣8, ♢8, ♡8, ♠8, ♣9, ♢9, ♡9, ♠9, ♣10, ♢10, ♡10, ♠10, ♣J, ♢J, ♡J, ♠J, ♣Q, ♢Q, ♡Q, ♠Q, ♣K, ♢K, ♡K, ♠K, ♣A, ♢A, ♡A, ♠A)
```

### Immutable Data Classes

- `position_frozen.py`: A frozen, immutable version of `Position`
- `immutable_deck.py`: Frozen `ImmutableCard` and `ImmutableDeck` classes, where the list of cards can still change

```pycon
>>> from position_frozen import Position
>>> pos = Position("Oslo", 10.8, 59.9)
>>> pos.name = "Stockholm"
Traceback (most recent call last):
  ...
dataclasses.FrozenInstanceError: cannot assign to field 'name'
```

### Inheritance

- `capital.py`: A `Capital` subclass that adds a `country` field to `Position`
- `capital_defaults.py`: A `Capital` subclass that redefines the default value of `lat`

```pycon
>>> from capital_defaults import Capital
>>> Capital("Madrid", country="Spain")
Capital(name='Madrid', lon=0.0, lat=40.0, country='Spain')
```

### Optimizing Data Classes

- `slots.py`: `SimplePosition` and `SlotPosition`, a regular data class and a data class with `slots=True`

```pycon
>>> from pympler import asizeof
>>> from slots import SimplePosition, SlotPosition
>>> simple = SimplePosition("London", -0.1, 51.5)
>>> slot = SlotPosition("Madrid", -3.7, 40.4)
>>> asizeof.asizesof(simple, slot)
(584, 152)
```
