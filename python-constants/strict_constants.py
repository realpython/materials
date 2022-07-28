# strict_constants.py

from collections import namedtuple
from dataclasses import dataclass


class ConstantsSpace__slots__:
    __slots__ = ()
    PI = 3.141592653589793
    EULER_NUMBER = 2.718281828459045


class ConstantsSpace_property:
    @property
    def PI(self):
        return 3.141592653589793

    @property
    def EULER_NUMBER(self):
        return 2.718281828459045


ConstantsSpace_namedtuple = namedtuple(
    "ConstantsSpace", ["PI", "EULER_NUMBER"]
)


@dataclass(frozen=True)
class ConstantsSpace_dataclass:
    PI = 3.141592653589793
    EULER_NUMBER = 2.718281828459045


class ConstantsSpace__setattr__:
    PI = 3.141592653589793
    EULER_NUMBER = 2.718281828459045

    def __setattr__(self, name, value):
        raise AttributeError(f"can't reassign constant '{name}'")
