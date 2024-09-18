def is_member(value, iterable):
    for current_value in iterable:
        if current_value == value:
            return True
    return False


print(is_member(5, [1, 2, 3, 4, 5]))
print(not is_member(5, [1, 2, 3, 4, 5]))
print(is_member(100, [1, 2, 3, 4, 5]))
print(not is_member(100, [1, 2, 3, 4, 5]))
