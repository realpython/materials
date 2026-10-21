# Python 3.15 or newer
NO_DEFAULT = sentinel("NO_DEFAULT")


def get_setting(config, path, default=NO_DEFAULT):
    current = config
    for part in path.split("."):
        try:
            current = current[part]
        except (KeyError, TypeError):
            if default is NO_DEFAULT:
                raise KeyError(path) from None
            return default
    return current
