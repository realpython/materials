from pathlib import Path

value = "Florina"

with Path("names.txt").open(mode="r", encoding="utf-8") as f:
    while (line := f.readline()) and value not in line:
        pass
    if line:
        print(f"Found: {line.strip()}")
    else:
        print("Not found")
