for i in (1, 2, 3, 4, 5):
    print(i)
else:
    print("The loop wasn't interrupted")

for i in (1, 2, 3, 4, 5):
    if i == 3:
        print("Number found:", i)
        break
else:
    print("Number not found")

for i in (1, 2, 3, 4, 5):
    if i == 3:
        continue
    print(i)
