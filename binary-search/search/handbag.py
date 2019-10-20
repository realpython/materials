"""
The handbag search algorithm.
"""

import random
from typing import Callable, Optional, Set, Sequence, Union

from search import T, S, identity


def find_index(elements: Sequence[T],
               value: S,
               key: Callable[[T], Union[T, S]] = identity) -> Optional[int]:
    """Return the index of value in elements or None."""
    visited: Set[int] = set()
    while len(visited) < len(elements):
        random_index = random.randint(0, len(elements) - 1)
        visited.add(random_index)
        if key(elements[random_index]) == value:
            return random_index
    return None


def find(elements: Sequence[T],
         value: S,
         key: Callable[[T], Union[T, S]] = identity) -> Optional[T]:
    """Return an element with matching key or None."""
    index = find_index(elements, value, key)
    return None if index is None else elements[index]


def contains(elements: Sequence[T],
             value: S,
             key: Callable[[T], Union[T, S]] = identity) -> bool:
    """Return True if value is present in elements."""
    return find_index(elements, value, key) is not None
