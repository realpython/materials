from collections import UserString


class MutableString(UserString):
    def __setitem__(self, index, value):
        data_as_list = list(self.data)
        data_as_list[index] = value
        self.data = "".join(data_as_list)

    def __delitem__(self, index):
        data_as_list = list(self.data)
        del data_as_list[index]
        self.data = "".join(data_as_list)

    def upper(self):
        self.data = self.data.upper()

    def lower(self):
        self.data = self.data.lower()

    def sort(self, key=None, reverse=False):
        self.data = "".join(sorted(self.data, key=key, reverse=reverse))
