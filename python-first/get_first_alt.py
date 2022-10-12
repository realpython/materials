from test_fixtures import countries


def find_match_gen(iterable, key=None, default=None):
    if callable(key):
        gen = (val for val in iterable if key(val))
    else:
        gen = (val for val in iterable if val)

    return next(gen, default)


if __name__ == "__main__":
    target_match = {"country": "Norway", "population": 5311916}
    print(find_match_gen(countries, target_match))

    def match_scotland(data):
        return data["country"] == "Scotland"

    print(find_match_gen(countries, key=match_scotland))
