import sys
from pathlib import Path
lazy import json

defaults = frozendict({"theme": "light", "autosave": True})
MISSING = sentinel("MISSING")

def resolve(overrides, name, default=MISSING):
    value = (defaults | overrides).get(name, default)
    return "unset" if value is MISSING else value

profiles = [{"theme": "crème brûlée"}, {"autosave": False}]
merged = {**profile for profile in profiles}
print("json imported:", "json" in sys.modules)
Path("user.json").write_text(json.dumps(defaults | merged, ensure_ascii=False))
print("json imported:", "json" in sys.modules)
print("theme:", resolve(merged, "theme"), "| font:", resolve(merged, "font"))
print(Path("user.json").read_text())
