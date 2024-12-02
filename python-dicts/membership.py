import timeit

MLB_teams = {
    "Colorado": "Rockies",
    "Chicago": "White Sox",
    "Boston": "Red Sox",
    "Minnesota": "Twins",
    "Milwaukee": "Brewers",
    "Seattle": "Mariners",
}

# Run timeit to compare the membership test
time_in_dict = timeit.timeit(
    '"Milwaukee" in MLB_teams', globals=globals(), number=1000000
)
time_in_keys = timeit.timeit(
    '"Milwaukee" in MLB_teams.keys()', globals=globals(), number=1000000
)
time_not_in_dict = timeit.timeit(
    '"Indianapolis" in MLB_teams', globals=globals(), number=1000000
)
time_not_in_keys = timeit.timeit(
    '"Indianapolis" in MLB_teams.keys()', globals=globals(), number=1000000
)

print(
    f"{time_in_dict     = } seconds",
    f"{time_in_keys     = } seconds",
    f"{time_not_in_dict = } seconds",
    f"{time_not_in_keys = } seconds",
    sep="\n",
)
