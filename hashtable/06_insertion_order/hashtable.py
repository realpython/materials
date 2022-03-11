# hashtable.py

from collections import deque
from typing import NamedTuple, Any


class Pair(NamedTuple):
    key: Any
    value: Any


class HashTable:
    @classmethod
    def from_dict(cls, dictionary, capacity=None):
        hash_table = cls(capacity or len(dictionary))
        for key, value in dictionary.items():
            hash_table[key] = value
        return hash_table

    def __init__(self, capacity=8, load_factor_threshold=0.6):
        if capacity < 1:
            raise ValueError("Capacity must be a positive number")
        if not (0 < load_factor_threshold <= 1):
            raise ValueError("Load factor must be a number between (0, 1]")
        self._keys = []
        self._buckets = [deque() for _ in range(capacity)]
        self._load_factor_threshold = load_factor_threshold

    def __len__(self):
        return len(self.pairs)

    def __iter__(self):
        yield from self.keys

    def __delitem__(self, key):
        match self._find(key):
            case bucket, index, _:
                del bucket[index]
                self._keys.remove(key)
            case _:
                raise KeyError(key)

    def __setitem__(self, key, value):
        if self.load_factor >= self._load_factor_threshold:
            self._resize_and_rehash()

        match self._find(key):
            case deque() as bucket, index, (key, _):
                bucket[index] = Pair(key, value)
            case bucket:
                bucket.append(Pair(key, value))
                self._keys.append(key)

    def __getitem__(self, key):
        match self._find(key):
            case _, _, pair:
                return pair.value
            case _:
                raise KeyError(key)

    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) is not type(other):
            return False
        return set(self.pairs) == set(other.pairs)

    def __str__(self):
        pairs = []
        for key, value in self.pairs:
            pairs.append(f"{key!r}: {value!r}")
        return "{" + ", ".join(pairs) + "}"

    def __repr__(self):
        cls = self.__class__.__name__
        return f"{cls}.from_dict({str(self)})"

    def copy(self):
        return HashTable.from_dict(dict(self.pairs), self.capacity)

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    @property
    def pairs(self):
        return [(key, self[key]) for key in self.keys]

    @property
    def values(self):
        return [self[key] for key in self.keys]

    @property
    def keys(self):
        return self._keys.copy()

    @property
    def capacity(self):
        return len(self._buckets)

    @property
    def load_factor(self):
        return len(self) / self.capacity

    def _index(self, key):
        return hash(key) % self.capacity

    def _resize_and_rehash(self):
        copy = HashTable(capacity=self.capacity * 2)
        for key, value in self.pairs:
            copy[key] = value
        self._buckets = copy._buckets

    def _find(self, key):
        bucket = self._buckets[self._index(key)]
        for index, pair in enumerate(bucket):
            if pair.key == key:
                return bucket, index, pair
        return bucket
