"""
Creating an infinite sequence of elements using generators
"""

import itertools

quarters = itertools.count(start=0, step=0.25)
# Print the first 8 elements, however, the sequence is infinite
for _ in range(8):
    print(next(quarters))

names = ["Sarah", "Matt", "Jim", "Denise", "Kate"]
rota = itertools.cycle(names)
print(rota)

print(next(rota))
print(next(rota))
print(next(rota))


# Use a generator function
def generate_rota(iterable):
    index = 0
    length = len(iterable)
    while True:
        yield iterable[index]
        if index == length - 1:
            index = 0
        else:
            index += 1


rota = generate_rota(names)
print("\nUsing a generator function")
for _ in range(12):
    print(next(rota))
