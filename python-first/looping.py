from test_cases import name_lists


def find_match_loop(iterable, value, default=None):
    if iterable is None:
        return default
    for val in iterable:
        if val == value:
            return val
    return default


if __name__ == "__main__":
    target_match = "Florina"
    default = None
    for name_list in name_lists:
        print(find_match_loop(target_match, name_list, default))
