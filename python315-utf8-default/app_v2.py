import json

from constants import ENCODING

with open("data.json", encoding=ENCODING) as f:
    data = json.load(f)

print(f"Loaded {len(data)} entries")
