def get_path(filename):
    """Return file's path or empty string if no path."""
    import os
    head, tail = os.path.split(filename)
    return head
