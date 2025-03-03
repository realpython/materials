def process_pairs(sequence):
    """Process a sequence, two elements at a time."""
    it = iter(sequence)
    while True:
        try:
            first = next(it)
            second = next(it)
        except StopIteration:
            break

        yield first, second


scientists = [
    "Newton",
    "Darwin",
    "Lovelace",
    "Freud",
    "Carver",
    "Curie",
    "Hopper",
    "Bohr",
]

print("Pairs of scientists:")
for first, second in process_pairs(scientists):
    print(f"- {first} and {second}")


print("\nWith zip()")
for first, second in zip(scientists[::2], scientists[1::2]):
    print(f"- {first} and {second}")
