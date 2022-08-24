import sys

try:
    raise ValueError("bpo-46328")
except ValueError:
    print(f"Handling {sys.exception()}")

# Typically you should prefer except ValueError as err:
try:
    raise ValueError("bpo-46328")
except ValueError as err:
    print(f"Handling {err}")
