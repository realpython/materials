import pickle
from profiles_legacy import _MISSING, parse_patch

patch = parse_patch({"name": "jane", "bio": None})
print(pickle.loads(pickle.dumps(patch))["email"] is _MISSING)
