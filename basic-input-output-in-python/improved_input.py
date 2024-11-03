import readline  # noqa F401

while (user_input := input("> ")).lower() != "exit":
    print("You entered:", user_input)
