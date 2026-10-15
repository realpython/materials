import timeit

numbers_list = list(range(100_000))

target = 99_999

list_time = timeit.timeit(lambda: target in numbers_list, number=1000)

print(target in numbers_list)
print(f"list membership: {list_time:.8f} seconds")
