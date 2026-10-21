# Python 3.14 and older approach
_NO_DEFAULT = object()


def get_setting(config, path, default=_NO_DEFAULT):
    current = config
    for part in path.split("."):
        try:
            current = current[part]
        except (KeyError, TypeError):
            if default is _NO_DEFAULT:
                raise KeyError(path) from None
            return default
    return current
