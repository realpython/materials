def my_enumerate(iterable, start=0):
    n = start
    for elem in iterable:
        yield n, elem
        n += 1


seasons = ["Spring", "Summer", "Fall", "Winter"]

print(my_enumerate(seasons))
print(list(my_enumerate(seasons)))
print(list(my_enumerate(seasons, start=1)))
