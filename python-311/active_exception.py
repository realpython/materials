import sys

try:
    raise ValueError("gh-90486")
except ValueError:
    print(f"Handling {sys.exception()}")

# Typically you should prefer except ValueError as err:
try:
    raise ValueError("gh-90486")
except ValueError as err:
    print(f"Handling {err}")
