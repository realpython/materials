"""
Split a Python List Into Fixed-Sized Chunks
"""

import math
import sys
from itertools import islice, zip_longest
from typing import Any, Iterable, Iterator, Sequence

import numpy as np


def batched(
    iterable: Iterable[Any], max_chunk_size: int
) -> Iterator[list[Any]]:
    if sys.version_info >= (3, 12):
        from itertools import batched

        return batched(iterable, max_chunk_size)
    try:
        from more_itertools import batched

        return batched(iterable, max_chunk_size)
    except ImportError:
        iterator = iter(iterable)
        while chunk := list(islice(iterator, max_chunk_size)):
            yield chunk


def batched_functional(
    iterable: Iterable[Any], max_chunk_size: int
) -> Iterator[list[Any]]:
    iterator = iter(iterable)
    return iter(lambda: list(islice(iterator, max_chunk_size)), [])


def split_with_padding(
    sequence: Iterable[Any], chunk_size: int, padding: Any = None
) -> Iterable[tuple[Any]]:
    return zip_longest(*[iter(sequence)] * chunk_size, fillvalue=padding)


def split_drop_last(
    sequence: Sequence[Any], chunk_size: int
) -> Iterator[Sequence[tuple[Any]]]:
    return zip(*[sequence[i::chunk_size] for i in range(chunk_size)])


def split_strings(
    sequence: Sequence[Any], max_chunk_size: int
) -> Iterator[Sequence[Any]]:
    for i in range(0, len(sequence), max_chunk_size):
        yield sequence[i : i + max_chunk_size]


def split_into_slices(
    sequence: Sequence[Any], max_chunk_size: int
) -> Iterator[slice]:
    for i in range(0, len(sequence), max_chunk_size):
        yield slice(i, i + max_chunk_size)


def split_list_with_padding(
    sequence: Sequence[Any], chunk_size: int, fill_with: Any
) -> Iterable[Sequence[Any]]:
    for i in range(0, len(sequence), chunk_size):
        chunk = list(sequence[i : i + chunk_size])
        padding = [fill_with] * (chunk_size - len(chunk))
        yield chunk + padding


def split_with_numpy(array: np.array, chunk_size: int) -> Iterable[np.array]:
    return np.array_split(array, math.ceil(len(array) / chunk_size))
