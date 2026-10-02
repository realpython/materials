"""
Different ways to create a 5x5 matrix initialized with zeros.

This file demonstrates three approaches for educational purposes.
"""


# 1️⃣ Using nested loops
matrix_loop = []
for row in range(5):
    matrix_loop.append([])
    for _ in range(5):
        matrix_loop[row].append(0)


# 2️⃣ Using list comprehension (recommended)
matrix_comprehension = [[0 for _ in range(5)] for _ in range(5)]


# 3️⃣ Using multiplication (be careful with nested lists!)
matrix_multiplication = [[0] * 5 for _ in range(5)]


if __name__ == "__main__":
    print("Matrix created using loops:")
    print(matrix_loop)

    print("\nMatrix created using list comprehension:")
    print(matrix_comprehension)

    print("\nMatrix created using multiplication:")
    print(matrix_multiplication)
