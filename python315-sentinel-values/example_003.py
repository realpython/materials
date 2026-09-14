import pickle
from copy import deepcopy

_MISSING = object()
print(_MISSING)
print(deepcopy(_MISSING) is _MISSING)
print(pickle.loads(pickle.dumps(_MISSING)) is _MISSING)
