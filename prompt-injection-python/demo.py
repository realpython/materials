import importlib
import sys

from corpus import CLEAN, PAYLOADS

module, payload = sys.argv[1], sys.argv[2]
app = importlib.import_module(module)
store = app.build_store([*CLEAN, PAYLOADS[payload]])
print(app.answer("How long does shipping take?", store))
