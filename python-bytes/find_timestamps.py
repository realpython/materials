import re
from pathlib import Path

binary_data = Path("picture.jpg").read_bytes()
pattern = rb"\d{4}:\d{2}:\d{2} \d{2}:\d{2}:\d{2}"

for match in re.finditer(pattern, binary_data):
    print(match)
