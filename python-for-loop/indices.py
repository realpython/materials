fruits = ["orange", "apple", "mango", "lemon"]

for index in range(len(fruits)):
    fruit = fruits[index]
    print(index, fruit)

for index, fruit in enumerate(fruits):
    print(index, fruit)
