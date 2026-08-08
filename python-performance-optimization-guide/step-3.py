import timeit
from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple"] * 1000


def manual_count(items):
    counts = {}
    for item in items:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


print(manual_count(words))

manual_time = timeit.timeit(lambda: manual_count(words), number=1000)
print(f"manual loop: {manual_time:.4f} seconds")


def counter_count(items):
    return Counter(items)


print(counter_count(words))

counter_time = timeit.timeit(lambda: counter_count(words), number=1000)
print(f"collections.Counter: {counter_time:.4f} seconds")
