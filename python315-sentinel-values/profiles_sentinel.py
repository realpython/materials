# Python 3.15 or newer
MISSING = sentinel("MISSING")


def parse_patch(form):
    fields = ("name", "bio", "email")
    return {field: form.get(field, MISSING) for field in fields}


def apply_patch(profile, patch):
    updated = dict(profile)
    for field, value in patch.items():
        if value is not MISSING:
            updated[field] = value
    return updated
