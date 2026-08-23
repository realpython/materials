import json

with open("data.json") as f:
    data = json.load(f)

print(f"Loaded {len(data)} entries")
