from copy import deepcopy


class _MissingType:
    def __repr__(self):
        return "MISSING"


MISSING = _MissingType()
print(MISSING)
print(deepcopy(MISSING) is MISSING)
