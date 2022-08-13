import timeit
from collections import UserList


class StringList_list(list):
    def __init__(self, iterable):
        super().__init__(str(item) for item in iterable)

    def __setitem__(self, index, item):
        super().__setitem__(index, str(item))

    def insert(self, index, item):
        super().insert(index, str(item))

    def append(self, item):
        super().append(str(item))

    def extend(self, other):
        if isinstance(other, type(self)):
            super().extend(other)
        else:
            super().extend(str(item) for item in other)


class StringList_UserList(UserList):
    def __init__(self, iterable):
        super().__init__(str(item) for item in iterable)

    def __setitem__(self, index, item):
        self.data[index] = str(item)

    def insert(self, index, item):
        self.data.insert(index, str(item))

    def append(self, item):
        self.data.append(str(item))

    def extend(self, other):
        if isinstance(other, type(self)):
            self.data.extend(other)
        else:
            self.data.extend(str(item) for item in other)


init_data = range(10000)

extended_list = StringList_list(init_data)
list_extend = (
    min(
        timeit.repeat(
            stmt="extended_list.extend(init_data)",
            number=5,
            repeat=2,
            globals=globals(),
        )
    )
    * 1e6
)

extended_user_list = StringList_UserList(init_data)
user_list_extend = (
    min(
        timeit.repeat(
            stmt="extended_user_list.extend(init_data)",
            number=5,
            repeat=2,
            globals=globals(),
        )
    )
    * 1e6
)

print(f"StringList_list().extend() time: {list_extend:.2f} μs")
print(f"StringList_UserList().extend() time: {user_list_extend:.2f} μs")
