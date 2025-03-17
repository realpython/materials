import hashlib
import sys
from pathlib import Path

python_path = Path(sys.executable)
checksum_path = python_path.with_suffix(".md5")

machine_code = python_path.read_bytes()
checksum_path.write_bytes(hashlib.md5(machine_code).digest())

print("Saved", checksum_path)
