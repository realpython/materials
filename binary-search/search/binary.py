"""
The binary search algorithm.
"""

from typing import Optional, Set, Sequence

from search import T, S, Key, identity


def find_index(
    elements: Sequence[T], value: S, key: Key = identity
) -> Optional[int]:
    """Return the index of value in elements or None."""

    left, right = 0, len(elements) - 1

    while left <= right:
        middle = (left + right) // 2

        middle_element = key(elements[middle])

        if middle_element == value:
            return middle

        if middle_element < value:
            left = middle + 1
        elif middle_element > value:
            right = middle - 1

    return None


def find_leftmost_index(
    elements: Sequence[T], value: S, key: Key = identity
) -> Optional[int]:
    """Return the leftmost index of value in elements or None."""

    index = find_index(elements, value, key)

    if index is not None:
        while index >= 0 and key(elements[index]) == value:
            index -= 1
        index += 1

    return index


def find_rightmost_index(
    elements: Sequence[T], value: S, key: Key = identity
) -> Optional[int]:
    """Return the rightmost index of value in elements or None."""

    index = find_index(elements, value, key)

    if index is not None:
        while index < len(elements) and key(elements[index]) == value:
            index += 1
        index -= 1

    return index


def find_all_indices(
    elements: Sequence[T], value: S, key: Key = identity
) -> Set[int]:
    """Return a set of indices of elements with matching key."""

    left = find_leftmost_index(elements, value, key)
    right = find_rightmost_index(elements, value, key)

    if left and right:
        return set(range(left, right + 1))

    return set()


def find(elements: Sequence[T], value: S, key: Key = identity) -> Optional[T]:
    """Return an element with matching key or None."""
    return _get(elements, find_index(elements, value, key))


def find_leftmost(
    elements: Sequence[T], value: S, key: Key = identity
) -> Optional[T]:
    """Return the leftmost element or None."""
    return _get(elements, find_leftmost_index(elements, value, key))


def find_rightmost(
    elements: Sequence[T], value: S, key: Key = identity
) -> Optional[T]:
    """Return the rightmost element or None."""
    return _get(elements, find_rightmost_index(elements, value, key))


def find_all(elements: Sequence[T], value: S, key: Key = identity) -> Set[T]:
    """Return a set of elements with matching key."""
    return {elements[i] for i in find_all_indices(elements, value, key)}


def contains(elements: Sequence[T], value: S, key: Key = identity) -> bool:
    """Return True if value is present in elements."""
    return find_index(elements, value, key) is not None


def _get(elements: Sequence[T], index: Optional[int]) -> Optional[T]:
    """Return element at the given index or None."""
    return None if index is None else elements[index]
