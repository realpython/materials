from profiles_legacy import apply_patch, parse_patch

patch = parse_patch({"name": "jane", "bio": None})
profile = {
    "name": "J. Doe",
    "bio": "Data scientist",
    "email": "jane@example.com",
}
print(apply_patch(profile, patch))
