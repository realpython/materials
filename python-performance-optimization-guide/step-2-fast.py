import timeit

numbers_list = list(range(100_000))
target = 99_999

numbers_set = set(numbers_list)

set_time = timeit.timeit(lambda: target in numbers_set, number=1000)

print(target in numbers_set)
print(f"set membership:  {set_time:.8f} seconds")