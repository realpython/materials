numbers = [1, 2, 3]
letters = ["a", "b", "c"]

for number, letter in zip(numbers, letters, strict=False):
    print(number, "->", letter)
