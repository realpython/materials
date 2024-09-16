line = input("Type some text: ")

while line != "stop":
    print(line)
    line = input("Type some text: ")


while True:
    line = input("Type some text: ")
    if line == "stop":
        break
    print(line)
