from typing import Tuple, Iterable, Any, List, Optional, Union
import array
import copy


DUMMY = -2
FREE = -1


class DictKey:
    def __init__(self, key, hashvalue):
        self.key = key
        self.hashvalue = hashvalue

    def __repr__(self):
        return f"<DictKey {self.key}>"


class Dictionary:
    __version = 0

    def __init__(self, *args, **kwargs):
        self._increase_version()
        self.indices = self._make_index_array(8)  # init with an 8 elements table
        self.keys: List[DictKey] = []
        self.values: List[Any] = []
        self.used = 0  # number of items in the dictionary
        self.filled = 0  # number of non-empty slots including dummy slots
        self.update(*args, **kwargs)

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
                dict_key = self.keys[entry_index]
                if dict_key.key is key or (
                    dict_key.hashvalue == hashvalue and dict_key.key == key
                ):
                    return (index, entry_index)

    def update(self, other=(), /, **kwargs):
        self._sharing_keys = False
        if isinstance(other, Dictionary):
            if self.used > 0:
                for key in other:
                    self[key] = other[key]
            else:
                self._sharing_keys = True
                self.indices = copy.copy(other.indices)
                self.keys = other.keys
                self.values = [None] * len(other.values)
                self.used = other.used
                self.filled = other.filled
        elif hasattr(other, "keys"):
            for key in other.keys():
                self[key] = other[key]
        else:
            for key, value in other:
                self[key] = value
        for key, value in kwargs.items():
            self[key] = value

    def _check_keys_sharing(self):
        """if trying to change dictionary with shared keys,
        migrate to non shared dictionary"""
        if self._sharing_keys:
            self.keys = copy.copy(self.keys)

    def __getitem__(self, key: Any) -> Any:
        hashvalue = hash(key)
        _, entry_index = self._lookup(key, hashvalue)
        if entry_index < 0:  # FREE or DUMMY
            raise KeyError(key)
        return self.values[entry_index]

    def __setitem__(self, key: Any, value: Any):
        self._check_keys_sharing()
        hashvalue = hash(key)
        indices_index, entry_index = self._lookup(key, hashvalue)
        if entry_index < 0:
            self._increase_version()
            self.indices[indices_index] = self.used
            dict_key = DictKey(key=key, hashvalue=hashvalue)
            self.keys.append(dict_key)
            self.values.append(value)
            self.used += 1
            if entry_index == FREE:
                self.filled += 1
                if self.filled / len(self.indices) > 2 / 3:
                    self._resize(4 * len(self))
        else:
            if value != self.values[entry_index]:
                self._increase_version()
                self.values[entry_index] = value

    def __delitem__(self, key: Any):
        self._check_keys_sharing()
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
            last_key_dict = self.keys[-1]
            last_value = self.values[-1]
            last_entry_indices_index, _ = self._lookup(
                last_key_dict.key, last_key_dict.hashvalue
            )
            self.indices[last_entry_indices_index] = entry_index
            self.keys[entry_index] = last_key_dict
            self.values[entry_index] = last_value
        self.keys.pop()
        self.values.pop()

    def _resize(self, n: int):
        n = 2 ** n.bit_length()
        self.indices = self._make_index_array(n)
        for entry_index, dict_key in enumerate(self.keys):
            for i in self._generate_probes(dict_key.hashvalue, n - 1):
                if self.indices[i] == FREE:
                    break
            self.indices[i] = entry_index
        self.filled = self.used

    def __contains__(self, key: Any) -> bool:
        _, entry_index = self._lookup(key, hash(key))
        return entry_index >= 0

    def __len__(self) -> int:
        return self.used

    def __iter__(self):
        return iter([dict_key.key for dict_key in self.keys])

    def __repr__(self) -> str:
        return f"<Dictionary keys={self.keys}, values={self.values}, version={self.__version}>"

    def show(self):
        """Used for nicely dispalying the dictionary"""
        print("=" * 50)
        print(f"Dictionary version {self.__version}")
        print("-" * 50)
        print(f"Indices: {list(self.indices)}")
        for i, row in enumerate(zip(self.keys, self.values)):
            print(i, row)
        print("=" * 50)


if __name__ == "__main__":
    d = Dictionary(
        [("key1", "value1"), ("key2", "value2"), (9, "different type of key")]
    )
    d.show()
    d["key1"] = "changed_value"
    d.show()
    del d["key2"]
    d.show()
    new_d = Dictionary(d)
    new_d["key1"] = "new_d_value"
    new_d.show()
    new_d["foo"] = "bazz"
    new_d.show()
    d.show()
    new_d.update(d)
    new_d.show()
