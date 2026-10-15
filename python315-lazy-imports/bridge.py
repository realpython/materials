import sys

__lazy_modules__ = {"json"}

import json

major, minor = sys.version_info[:2]
deferred = "json" in getattr(sys, "lazy_modules", ())
print(f"Python {major}.{minor}: json deferred? {deferred}")
print(json.dumps({"ok": True}))
