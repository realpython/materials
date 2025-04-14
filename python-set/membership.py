import random
import time

numbers_list = list(range(1_000_000))
numbers_set = set(range(1_000_000))
number_to_check = [random.randint(0, 999_999) for _ in range(1_000)]

start = time.perf_counter()
for number in number_to_check:
    _ = number in numbers_list
end = time.perf_counter()
print(f"List membership check took {end - start:.4f} seconds")

start = time.perf_counter()
for number in number_to_check:
    _ = number in numbers_set
end = time.perf_counter()
print(f"Set membership check took {end - start:.4f} seconds")
