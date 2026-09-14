import pickle
from copy import deepcopy
from profiles_sentinel import MISSING, parse_patch

patch = parse_patch({"name": "jane", "bio": None})
print(deepcopy(patch)["email"] is MISSING)
print(pickle.loads(pickle.dumps(patch))["email"] is MISSING)
