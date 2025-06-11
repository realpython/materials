import readline  # noqa

print('Type "help", "exit", "add a [b [c ...]]"')
while True:
    command, *arguments = input("~ ").split(" ")
    if len(command) > 0:
        if command.lower() == "exit":
            break
        elif command.lower() == "help":
            print("This is help.")
        elif command.lower() == "add":
            print(sum(map(int, arguments)))
        else:
            print("Unknown command")
