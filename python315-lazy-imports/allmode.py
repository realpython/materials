import sys

import json

print("json deferred?", "json" in sys.lazy_modules)
print(json.dumps({"ok": True}))
