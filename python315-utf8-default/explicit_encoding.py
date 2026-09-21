import json

with open("data.json", encoding="utf-8") as f:  # Portable and unambiguous
    data = json.load(f)

with open("legacy.csv", encoding="locale") as f:  # Intentional locale use
    legacy = f.read()
