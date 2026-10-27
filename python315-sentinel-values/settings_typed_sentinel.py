# Python 3.15 or newer, with type hints
NO_DEFAULT = sentinel("NO_DEFAULT")


def get_setting(
    config: dict[str, object],
    path: str,
    default: str | int | NO_DEFAULT = NO_DEFAULT,
) -> str | int:
    current = config
    for part in path.split("."):
        try:
            current = current[part]
        except (KeyError, TypeError):
            if default is NO_DEFAULT:
                raise KeyError(path) from None
            return default
    return current
