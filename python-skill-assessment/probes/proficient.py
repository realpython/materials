def evens_below(n):
    for number in range(n):
        if number % 2 == 0:
            yield number


print(list(evens_below(7)))
print(list(evens_below(0)))
