numbers = range(5)

squares = []
for n in numbers:
    squares.append(n * n)

assert squares == [n * n for n in numbers]
print(squares)
