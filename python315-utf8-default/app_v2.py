from constants import ENCODING

with open("data.json", encoding=ENCODING) as f:
    data = f.read()

print(f"Loaded {len(data)} entries")
