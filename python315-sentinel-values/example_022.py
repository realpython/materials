import pickle
from copy import deepcopy
from profiles_sentinel import MISSING, apply_patch, parse_patch

profile = {
    "name": "J. Doe",
    "bio": "Data scientist",
    "email": "jane@example.com",
}
patch = parse_patch({"name": "jane", "bio": None})
print(deepcopy(patch)["email"] is MISSING)
print(pickle.loads(pickle.dumps(patch))["email"] is MISSING)
print(apply_patch(profile, deepcopy(patch)))
