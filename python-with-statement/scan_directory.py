import os

with os.scandir(".") as dir_entries:
    for entry in dir_entries:
        print(entry.name, "->", entry.stat().st_size, "bytes")
