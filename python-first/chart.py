from timeit import timeit

import matplotlib.pyplot as plt

from generator import find_match_gen
from looping import find_match_loop
from test_cases import build_list

TIMEIT_TIMES = 10_000
LIST_SIZE = 1_000
POSITION_INCREMENT = 10

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
        LIST_SIZE, "Fake Python", "Real Python", position
    )

    looping_times.append(
        timeit(
            "find_match_loop(list_to_search, 'Real Python', None)",
            globals=globals(),
            number=TIMEIT_TIMES,
        )
    )
    generator_times.append(
        timeit(
            "find_match_gen(list_to_search, 'Real Python', None)",
            globals=globals(),
            number=TIMEIT_TIMES,
        )
    )

print("Progress 100%")

fig, ax = plt.subplots()

plot = ax.plot(positions, looping_times)
plot = ax.plot(positions, generator_times)

plt.xlim([0, LIST_SIZE])
plt.ylim([0, max(max(looping_times), max(generator_times))])

plt.show()
