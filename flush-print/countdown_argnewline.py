from time import sleep

for second in range(3, 0, -1):
    print(f"{second}\n", end="")
    sleep(1)
print("Go!")
