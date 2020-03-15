from typing import Tuple, Iterable, Any, List, Optional, Union
import array

DUMMY = -2
FREE = -1


class Entry:
    def __init__(self, key, value, hashvalue):
        self.key = key
        self.value = value
        self.hashvalue = hashvalue

    def __repr__(self):
        return f"<Entry key={self.key}, value={self.value}>"


class Dictionary:
    __version = 0

    def __init__(self, pairs: list = []):
        self._increase_version()
        self.indices = self._make_index_array(8)  # init with an 8 elements table
        self.entries: List[Any] = []
        self.used = 0  # number of items in the dictionary
        self.filled = 0  # number of non-empty slots including dummy slots
        for key, value in pairs:
            self.__setitem__(key, value)

    def _increase_version(self):
        self.__version = Dictionary.__version
        Dictionary.__version += 1

    @staticmethod
    def _make_index_array(n: int) -> Union[list, array.array]:
        "New sequence of indices using the smallest possible datatype"
        if n <= 2 ** 7:
            return array.array("b", [FREE]) * n  # signed char
        if n <= 2 ** 15:
            return array.array("h", [FREE]) * n  # signed short
        if n <= 2 ** 31:
            return array.array("l", [FREE]) * n  # signed long
        return [FREE] * n

    @staticmethod
    def _generate_probes(hash_: int, mask: int) -> Iterable[int]:
        index = hash_ & mask
        yield index
        perturb = hash_
        while True:
            new_hash = index * 5 + 1 + perturb
            yield new_hash & mask
            perturb >>= 5

    def _lookup(self, key: Any, hashvalue: int) -> Tuple[int, Any]:
        mask = len(self.indices) - 1
        freeslot = None
        for index in self._generate_probes(hashvalue, mask):
            entry_index = self.indices[index]
            if entry_index == FREE:
                return (index, FREE) if freeslot is None else (freeslot, DUMMY)
            elif entry_index == DUMMY:
                if freeslot is None:
                    freeslot = index
            else:
                entry = self.entries[entry_index]
                if entry.key is key or (
                    entry.hashvalue == hashvalue and entry.key == key
                ):
                    return (index, entry_index)

    def __getitem__(self, key: Any) -> Any:
        hashvalue = hash(key)
        _, entry_index = self._lookup(key, hashvalue)
        if entry_index < 0:  # FREE or DUMMY
            raise KeyError(key)
        return self.entries[entry_index].value

    def __setitem__(self, key: Any, value: Any):
        hashvalue = hash(key)
        indices_index, entry_index = self._lookup(key, hashvalue)
        if entry_index < 0:
            self._increase_version()
            self.indices[indices_index] = self.used
            entry = Entry(key=key, value=value, hashvalue=hashvalue)
            self.entries.append(entry)
            self.used += 1
            if entry_index == FREE:
                self.filled += 1
                if self.filled / len(self.indices) > 2 / 3:
                    self._resize(4 * len(self))
        else:
            if value != self.entries[entry_index].value:
                self._increase_version()
                self.entries[entry_index].value = value

    def __delitem__(self, key: Any):
        hashvalue = hash(key)
        indices_index, entry_index = self._lookup(key, hashvalue)
        if entry_index < 0:
            raise KeyError(key)

        self._increase_version()
        self.used -= 1
        self.indices[indices_index] = DUMMY
        # del self.entries[entry_index]
        # swap with the last item to avoid holes
        if entry_index != self.used:
            last_entry = self.entries[-1]
            last_entry_indices_index, _ = self._lookup(
                last_entry.key, last_entry.hashvalue
            )
            self.indices[last_entry_indices_index] = entry_index
            self.entries[entry_index] = last_entry
        self.entries.pop()

    def _resize(self, n: int):
        n = 2 ** n.bit_length()
        self.indices = self._make_index_array(n)
        for entry_index, entry in enumerate(self.entries):
            for i in self._generate_probes(entry.hashvalue, n - 1):
                if self.indices[i] == FREE:
                    break
            self.indices[i] = entry_index
        self.filled = self.used

    def __contains__(self, key: Any) -> bool:
        _, entry_index = self._lookup(key, hash(key))
        return entry_index >= 0

    def __len__(self) -> int:
        return self.used

    def __repr__(self) -> str:
        return f"<Dictionary {self.entries}, version={self.__version}>"


if __name__ == "__main__":
    d = Dictionary(
        [("key1", "value1"), ("key2", "value2"), (1, "different type of key")]
    )
    print(d)
    print(d["key1"])
    d["key1"] = "changed_value"
    print(d)
    del d["key2"]
    print(d)
