from copy import copy, deepcopy

MISSING = sentinel("MISSING")
print(copy(MISSING) is MISSING)
print(deepcopy(MISSING) is MISSING)
