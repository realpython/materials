from test_fixtures import countries


def get_first(iterable, value=None, key=None, default=None):
    match value is None, callable(key):
        case (True, True):
            gen = (elem for elem in iterable if key(elem))
        case (False, True):
            gen = (elem for elem in iterable if key(elem) == value)
        case (True, False):
            gen = (elem for elem in iterable if elem)
        case (False, False):
            gen = (elem for elem in iterable if elem == value)

    return next(gen, default)


if __name__ == "__main__":
    print(get_first(countries))

    target_match = {"country": "Norway", "population": 5_311_916}
    print(get_first(countries, value=target_match))

    def match_scotland(data):
        return data["country"] == "Scotland"

    print(get_first(countries, key=match_scotland))
