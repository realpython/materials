# With assignment operator
while (line := input("Type some text: ")) != "stop":
    print(line)


# With assignment before loop
line = input("Type some text: ")

while line != "stop":
    print(line)
    line = input("Type some text: ")


# With condition inside loop
while True:
    line = input("Type some text: ")
    if line == "stop":
        break
    print(line)
