def count_up_to(n):
    yield from range(1, n + 1)


print(list(count_up_to(3)))
print(list(count_up_to(0)))
