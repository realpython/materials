"""
Split a Python List Into a Fixed Number of Chunks With Roughly Equal Sizes
"""

from itertools import zip_longest
from typing import Any, Iterable, Iterator, Sequence

import numpy as np


def split_with_numpy(array: np.array, num_chunks: int) -> Iterable[np.array]:
    return np.array_split(array, num_chunks)


def split_transposed(
    sequence: Sequence[Any], num_chunks: int
) -> Iterator[tuple[Any]]:
    for i in range(num_chunks):
        yield sequence[i::num_chunks]


def transpose(chunks, padding: Any = None) -> Iterator[tuple[Any]]:
    return zip_longest(*chunks, value=padding)


def split(sequence: Sequence[Any], num_chunks: int) -> Iterator[Sequence[Any]]:
    chunk_size, remaining = divmod(len(sequence), num_chunks)
    for i in range(num_chunks):
        begin = i * chunk_size + min(i, remaining)
        end = (i + 1) * chunk_size + min(i + 1, remaining)
        yield sequence[begin:end]
