squares = {}

for integer in range(1, 10):
    squares[integer] = integer**2

print(squares)

squares = {integer: integer**2 for integer in range(1, 10)}

print(squares)
