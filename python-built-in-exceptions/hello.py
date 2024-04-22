try:
    with open("hello.txt", mode="x") as file:
        file.write("Hello, World!")
except FileExistsError:
    print("The file already exists")

try:
    with open("hello.txt", mode="r") as file:
        print(file.read())
except FileNotFoundError:
    print("The file doesn't exist.")
