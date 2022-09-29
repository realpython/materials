import string
from enum import Enum


class BaseTextEnum(Enum):
    def as_list(self):
        try:
            return list(self.value)
        except TypeError:
            return [str(self.value)]


class Alphabet(BaseTextEnum):
    LOWERCASE = string.ascii_lowercase
    UPPERCASE = string.ascii_uppercase


print(Alphabet.LOWERCASE.as_list())
