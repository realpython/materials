# Python 3.14 and older approach
_MISSING = object()


def parse_patch(form):
    fields = ("name", "bio", "email")
    return {field: form.get(field, _MISSING) for field in fields}


def apply_patch(profile, patch):
    updated = dict(profile)
    for field, value in patch.items():
        if value is not _MISSING:
            updated[field] = value
    return updated
