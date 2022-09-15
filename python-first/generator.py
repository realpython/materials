from test_cases import name_lists


def find_match_gen(iterable, value, default=None):
    if iterable is None:
        return default
    return next((val for val in iterable if val == value), default)


if __name__ == "__main__":
    target_match = "Florina"
    default = None
    for name_list in name_lists:
        print(find_match_gen(target_match, name_list))
