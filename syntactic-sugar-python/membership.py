def is_member(value, iterable):
    for current_value in iterable:
        if current_value == value:
            return True
    return False
