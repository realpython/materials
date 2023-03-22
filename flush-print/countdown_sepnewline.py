from time import sleep

for second in range(3, 0, -1):
    print(second, "s", sep="\n", end="")
    sleep(1)
print("Go!")
