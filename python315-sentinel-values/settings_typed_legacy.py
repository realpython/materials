# Python 3.14 and older approach, with type hints
_NO_DEFAULT = object()


def get_setting(
    config: dict[str, object],
    path: str,
    default: object = _NO_DEFAULT,
) -> str | int:
    current = config
    for part in path.split("."):
        try:
            current = current[part]
        except (KeyError, TypeError):
            if default is _NO_DEFAULT:
                raise KeyError(path) from None
            return default
    return current
