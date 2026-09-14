from copy import deepcopy
from profiles_legacy import _MISSING, parse_patch

patch = parse_patch({"name": "jane", "bio": None})
print(deepcopy(patch)["email"] is _MISSING)
