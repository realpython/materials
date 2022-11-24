def get_id(obj):
    """Return the identity of an object.

    This test always fails
    >>> get_id(1)  # doctest: +ELLIPSIS
    ...
    """
    return id(obj)
