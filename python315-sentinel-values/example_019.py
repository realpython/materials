from profiles_legacy import apply_patch, parse_patch

profile = {
    "name": "J. Doe",
    "bio": "Data scientist",
    "email": "jane@example.com",
}
patch = parse_patch({"name": "jane", "bio": None})
print(apply_patch(profile, patch))
