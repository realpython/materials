from pathlib import Path

value = "Florina"

with open(Path("names.txt"), mode="r", encoding="utf-8") as f:
    while value not in (line := f.readline()) and line != "":
        pass
    if line != "":
        print(f"Found: {line.strip()}")
    else:
        print("Not found")
