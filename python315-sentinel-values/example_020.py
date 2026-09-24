from copy import deepcopy
from profiles_legacy import _MISSING, apply_patch, parse_patch

profile = {
    "name": "J. Doe",
    "bio": "Data scientist",
    "email": "jane@example.com",
}
patch = parse_patch({"name": "jane", "bio": None})
print(deepcopy(patch)["email"] is _MISSING)
print(apply_patch(profile, deepcopy(patch)))
