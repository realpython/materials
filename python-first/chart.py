from timeit import timeit

import matplotlib.pyplot as plt

from test_fixtures import build_list

TIMEIT_TIMES = 100_000
LIST_SIZE = 500
POSITION_INCREMENT = 10

looping_times = []
generator_times = []
in_times = []
positions = []


def find_match_loop(list_to_search, item_to_find):
    for val in list_to_search:
        if val == item_to_find:
            return val
    return None


def find_match_gen(list_to_search, item_to_find):
    return next((val for val in list_to_search if val == item_to_find), None)


def find_match_in(list_to_search, item_to_find):
    if item_to_find in list_to_search:
        return item_to_find


for position in range(0, LIST_SIZE, POSITION_INCREMENT):
    print(
        f"Progress {position/LIST_SIZE:.0%}",
        end=f"{3 * ' '}\r",  # Clear previous characters and resets cursor
    )

    positions.append(position)

    list_to_search = build_list(
        LIST_SIZE, "Fake Python", "Real Python", position
    )

    looping_times.append(
        timeit(
            "find_match_loop(list_to_search, 'Real Python')",
            globals=globals(),
            number=TIMEIT_TIMES,
        )
    )
    generator_times.append(
        timeit(
            "find_match_gen(list_to_search, 'Real Python')",
            globals=globals(),
            number=TIMEIT_TIMES,
        )
    )
    in_times.append(
        timeit(
            "find_match_in(list_to_search, 'Real Python')",
            globals=globals(),
            number=TIMEIT_TIMES,
        )
    )

print("Progress 100%")

fig, ax = plt.subplots()

plot = ax.plot(positions, looping_times, label="loop")
plot = ax.plot(positions, generator_times, label="generator")
plot = ax.plot(positions, in_times, label="in")

plt.xlim([0, LIST_SIZE])
plt.xlabel("Position of element to be found")
plt.ylim([0, max(max(looping_times), max(generator_times))])
plt.ylabel(f"Time to complete {TIMEIT_TIMES:,} times")
plt.legend()

plt.show()
