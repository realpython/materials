from collections import Counter
import timeit

words = ["apple", "pear", "apple", "cherry", "pear", "apple"] * 1000


def counter_count(items):
    return Counter(items)


print(counter_count(words))

counter_time = timeit.timeit(lambda: counter_count(words), number=1000)
print(f"collections.Counter: {counter_time:.4f} seconds")
