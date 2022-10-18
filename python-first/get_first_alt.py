from test_fixtures import countries


def get_first(iterable, default=None, key=None):
    if callable(key):
        gen = (elem for elem in iterable if key(elem))
    else:
        gen = (elem for elem in iterable if elem)

    return next(gen, default)


if __name__ == "__main__":
    print(get_first(countries))

    target_match = {"country": "Norway", "population": 5_311_916}
    print(get_first(countries, key=lambda elem: elem == target_match))

    def match_scotland(data):
        return data["country"] == "Scotland"

    print(get_first(countries, key=match_scotland))
