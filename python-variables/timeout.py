_timeout = 30  # in seconds


def get_timeout():
    return _timeout


def set_timeout(seconds):
    global _timeout
    _timeout = seconds
