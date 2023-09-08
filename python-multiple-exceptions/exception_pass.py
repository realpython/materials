try:
    with open("file.txt", mode="rt") as f:
        print(f.readlines())
except (FileNotFoundError, PermissionError):
    pass
