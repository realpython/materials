import perfplot


def build_list(size, fill, value, at_position):
    return [value if i == at_position else fill for i in range(size)]


def find_match_loop(iterable):
    for value in iterable:
        if value["population"] > 50:
            return value
    return None


def find_match_gen(iterable):
    return next(
        (value for value in iterable if value["population"] > 50), None
    )


perfplot.show(
    n_range=[2**n for n in range(25)],
    setup=lambda n: build_list(
        size=n,
        fill={"country": "Nowhere", "population": 10},
        value={"country": "Atlantis", "population": 100},
        at_position=n // 2,
    ),
    kernels=[find_match_loop, find_match_gen],
    labels=["loop", "gen"],
    equality_check=None,
    relative_to=0,
)
