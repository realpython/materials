import enum


class MissingType(enum.Enum):
    MISSING = "MISSING"


print(repr(MissingType.MISSING))
