from time import sleep

for second in range(3, 0, -1):
    print(second, flush=True)
    sleep(1)
print("Go!")
