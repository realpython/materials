import string
from enum import Enum


class BaseTextEnum(Enum):
    def as_list(self):
        if not len(self.value):
            raise NotImplementedError("empty enum member")
        return [item for item in self.value]


class Alphabet(BaseTextEnum):
    LOWERCASE = string.ascii_lowercase
    UPPERCASE = string.ascii_uppercase


print(Alphabet.LOWERCASE.as_list())
