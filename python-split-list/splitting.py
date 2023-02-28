"""
Split into fixed-size chunks or a fixed number of chunks.
"""

import sys
from itertools import cycle, islice, zip_longest
from typing import Any, Iterable, Iterator, Sequence

import numpy as np

if sys.version_info >= (3, 12):
    from itertools import batched
else:
    try:
        from more_itertools import batched
    except ImportError:

        def batched(
            iterable: Iterable[Any], chunk_size: int
        ) -> Iterator[tuple[Any, ...]]:
            iterator = iter(iterable)
            while chunk := tuple(islice(iterator, chunk_size)):
                yield chunk


def batched_with_padding(
    iterable: Iterable[Any], batch_size: int, fill_value: Any = None
) -> Iterator[tuple[Any, ...]]:
    for batch in batched(iterable, batch_size):
        yield batch + (fill_value,) * (batch_size - len(batch))


def batched_functional(
    iterable: Iterable[Any], chunk_size: int
) -> Iterator[tuple[Any, ...]]:
    iterator = iter(iterable)
    return iter(lambda: tuple(islice(iterator, chunk_size)), tuple())


def split_with_padding(
    iterable: Iterable[Any], chunk_size: int, fill_value: Any = None
) -> Iterator[tuple[Any, ...]]:
    return zip_longest(*[iter(iterable)] * chunk_size, fillvalue=fill_value)


def split_into_pairs(
    iterable: Iterable[Any], fill_value: Any = None
) -> Iterator[tuple[Any, Any]]:
    iterator = iter(iterable)
    return zip_longest(iterator, iterator, fillvalue=fill_value)


def split_drop_last(
    iterable: Iterable[Any], chunk_size: int
) -> Iterator[tuple[Any, ...]]:
    return zip(*[iter(iterable)] * chunk_size)


def split_sequence(
    sequence: Sequence[Any], chunk_size: int
) -> Iterator[Sequence[Any]]:
    for i in range(0, len(sequence), chunk_size):
        yield sequence[i : i + chunk_size]


def split_str(
    sequence: str, chunk_size: int, fill_value: str = " "
) -> Iterator[str]:
    for chunk in split_sequence(sequence, chunk_size):
        padding = "".join([fill_value] * (chunk_size - len(chunk)))
        yield chunk + padding


def split_list(
    sequence: list[Any], chunk_size: int, fill_value: Any = None
) -> Iterator[list[Any]]:
    for chunk in split_sequence(sequence, chunk_size):
        padding = [fill_value] * (chunk_size - len(chunk))
        yield chunk + padding


def split_into_slices(
    sequence: Sequence[Any], slice_size: int
) -> Iterator[slice]:
    for i in range(0, len(sequence), slice_size):
        yield slice(i, i + slice_size)


def split_strides(
    sequence: Sequence[Any], num_chunks: int
) -> Iterator[Sequence[Any]]:
    for i in range(num_chunks):
        yield sequence[i::num_chunks]


def split_round_robin(
    iterable: Iterable[Any], num_chunks: int
) -> list[list[Any]]:
    chunks: list[list[Any]] = [list() for _ in range(num_chunks)]
    index = cycle(range(num_chunks))
    for value in iterable:
        chunks[next(index)].append(value)
    return chunks


def split_n(
    sequence: Sequence[Any], num_chunks: int
) -> Iterator[Sequence[Any]]:
    chunk_size, remaining = divmod(len(sequence), num_chunks)
    for i in range(num_chunks):
        begin = i * chunk_size + min(i, remaining)
        end = (i + 1) * chunk_size + min(i + 1, remaining)
        yield sequence[begin:end]


def split_with_numpy(
    numbers: Sequence[float | int], chunk_size: int
) -> list[np.ndarray]:
    indices = np.arange(chunk_size, len(numbers), chunk_size)
    return np.array_split(numbers, indices)
