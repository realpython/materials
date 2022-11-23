import sys

try:
    raise SystemExit(sys.argv[1])
except IndexError as e:
    raise SystemExit(0) from e
