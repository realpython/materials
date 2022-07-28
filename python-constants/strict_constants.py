# strict_constants.py

from collections import namedtuple
from dataclasses import dataclass


class ConstantsNamespace__slots__:
    __slots__ = ()
    PI = 3.141592653589793
    EULER_NUMBER = 2.718281828459045


class ConstantsNamespace_property:
    @property
    def PI(self):
        return 3.141592653589793

    @property
    def EULER_NUMBER(self):
        return 2.718281828459045


ConstantsNamespace_namedtuple = namedtuple(
    "ConstantsNamespace", ["PI", "EULER_NUMBER"]
)


@dataclass(frozen=True)
class ConstantsNamespace_dataclass:
    PI = 3.141592653589793
    EULER_NUMBER = 2.718281828459045


class ConstantsNamespace__setattr__:
    PI = 3.141592653589793
    EULER_NUMBER = 2.718281828459045

    def __setattr__(self, name, value):
        raise AttributeError(f"can't reassign constant '{name}'")
