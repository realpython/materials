from timeit import timeit

a_list = list(range(100_000))
a_set = set(range(100_000))


list_time = timeit("-1 in a_list", number=1, globals=globals())
set_time = timeit("-1 in a_set", number=1, globals=globals())

print(f"Sets are {(list_time / set_time):.2f} times faster than Lists")
