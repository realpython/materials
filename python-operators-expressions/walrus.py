def validate_length(string):
    if (n := len(string)) < 8:
        print(f"Length {n} is too short, needs at least 8")
    else:
        print(f"Length {n} is okay!")


validate_length("Pythonista")
validate_length("Python")
