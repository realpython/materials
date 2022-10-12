"""
Script to chart out the performance of generators and loops for finding the
first matching element in a list.
"""

from timeit import timeit

import matplotlib.pyplot as plt


TIMEIT_TIMES = 100  # Increase number for smoother lines
LIST_SIZE = 1000
POSITION_INCREMENT = 10


def find_match_loop(iterable):
    for val in iterable:
        if val["population"] > 50:
            return val


def find_match_gen(iterable):
    return next(val for val in iterable if val["population"] > 50)


def build_list(size, fill, value, at_position):
    return [fill if i != at_position else value for i in range(size)]


looping_times = []
generator_times = []
positions = []

for position in range(0, LIST_SIZE, POSITION_INCREMENT):
    print(
        f"Progress {position/LIST_SIZE:.0%}",
        end=f"{3 * ' '}\r",  # Clear previous characters and reset cursor
    )

    positions.append(position)

    list_to_search = build_list(
        LIST_SIZE,
        {"country": "Oceania", "population": 10},
        {"country": "Atlantis", "population": 100},
        position,
    )

    looping_times.append(
        timeit(
            "find_match_loop(list_to_search)",
            globals=globals(),
            number=TIMEIT_TIMES,
        )
    )
    generator_times.append(
        timeit(
            "find_match_gen(list_to_search)",
            globals=globals(),
            number=TIMEIT_TIMES,
        )
    )

print("Progress 100%")

fig, ax = plt.subplots()

plot = ax.plot(positions, looping_times, label="loop")
plot = ax.plot(positions, generator_times, label="generator")

plt.xlim([0, LIST_SIZE])
plt.xlabel("Position of element to be found")
plt.ylim([0, max(max(looping_times), max(generator_times))])
plt.ylabel(f"Time to complete {TIMEIT_TIMES:,} times")
plt.legend()

plt.show()

# Ratio

looping_ratio = [loop / loop for loop in looping_times]
generator_ratio = [
    gen / loop for gen, loop in zip(generator_times, looping_times)
]

fig, ax = plt.subplots()

plot = ax.plot(positions, looping_ratio, label="loop")
plot = ax.plot(positions, generator_ratio, label="generator")

plt.xlim([0, LIST_SIZE])
plt.xlabel("Position of element to be found")
plt.ylim([0, max(max(looping_ratio), max(generator_ratio))])
plt.ylabel(f"Time to complete {TIMEIT_TIMES:,} times")
plt.legend()

plt.show()
