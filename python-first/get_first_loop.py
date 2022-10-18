from test_fixtures import countries


def get_first_loop_no_key(iterable, value=None, default=None):
    for elem in iterable:
        if (value is None and elem) or (value is not None and elem == value):
            return elem
    return default


def get_first_loop(iterable, value=None, key=None, default=None):
    for elem in iterable:
        _elem = key(elem) if callable(key) else elem

        if (value is None and _elem) or (value is not None and _elem == value):
            return elem
    return default


if __name__ == "__main__":
    print(get_first_loop(countries))

    target_match = {"country": "Dominican Republic", "population": 10_627_165}
    print(get_first_loop(countries, value=target_match))

    def match_scotland(data):
        return data["country"] == "Scotland"

    print(get_first_loop(countries, key=match_scotland))
