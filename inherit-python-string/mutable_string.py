from collections import UserString


class MutableString(UserString):
    def __setitem__(self, index, value):
        self.data = self.data.replace(self.data[index], value)

    def __delitem__(self, index):
        self.data = self.data[: index - 1] + self.data[index:]

    def upper(self):
        self.data = self.data.upper()

    def lower(self):
        self.data = self.data.lower()

    def sort(self, key=None, reverse=False):
        self.data = "".join(sorted(self.data, key=key, reverse=reverse))
