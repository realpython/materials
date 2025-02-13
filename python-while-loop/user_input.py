line = input("Type some text: ")

while line != "stop":
    print(line)
    line = input("Type some text: ")


while (line := input("Type some text: ")) != "stop":
    print(line)
