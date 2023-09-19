"""
Script to chart out the performance of generators, loops and the in operator
when trying to find the first matching element in a list.
"""

from timeit import timeit

import matplotlib.pyplot as plt

TIMEIT_TIMES = 100  # Increase number for smoother lines
LIST_SIZE = 1000
POSITION_INCREMENT = 10

looping_times = []
generator_times = []
in_times = []
positions = []


def build_list(size, fill, value, at_position):
    return [value if i == at_position else fill for i in range(size)]


def find_match_loop(list_to_search, item_to_find):
    for value in list_to_search:
        if value == item_to_find:
            return value
    return None


def find_match_gen(list_to_search, item_to_find):
    return next(
        (value for value in list_to_search if value == item_to_find), None
    )


def find_match_in(list_to_search, item_to_find):
    if item_to_find in list_to_search:
        return item_to_find


for position in range(0, LIST_SIZE, POSITION_INCREMENT):
    print(
        f"Progress {position / LIST_SIZE:.0%}",
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
plt.ylim([0, max(max(looping_times), max(generator_times), max(in_times))])

plt.xlabel("Index of element to be found")
plt.ylabel(f"Time in seconds to find element {TIMEIT_TIMES:,} times")
plt.title("Raw Time to Find First Match")
plt.legend()

plt.show()

# Ratio

looping_ratio = [loop / loop for loop in looping_times]
generator_ratio = [
    gen / loop for gen, loop in zip(generator_times, looping_times)
]
in_ratio = [in_ / loop for in_, loop in zip(in_times, looping_times)]

fig, ax = plt.subplots()

plot = ax.plot(positions, looping_ratio, label="loop")
plot = ax.plot(positions, generator_ratio, label="generator")
plot = ax.plot(positions, in_ratio, label="in")

plt.xlim([0, LIST_SIZE])
plt.ylim([0, max(max(looping_ratio), max(generator_ratio), max(in_ratio))])
plt.xlabel("Index of element to be found")
plt.ylabel("Speed to find element, relative to loop")
plt.title("Relative Speed to Find First Match")
plt.legend()

plt.show()
