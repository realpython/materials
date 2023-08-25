# exception_suppress.py

from contextlib import suppress

with suppress(FileNotFoundError, PermissionError):
    with open("file.txt", mode="rt") as f:
        print(f.readlines())
