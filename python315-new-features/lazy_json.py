import sys

lazy import json

print("json loaded:", "json" in sys.modules)
config = json.dumps({"theme": "dark", "autosave": True})
print("json loaded:", "json" in sys.modules)
print(config)
