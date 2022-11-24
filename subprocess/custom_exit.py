import sys

print(sys.argv)

try:
    raise SystemExit(int(sys.argv[1]))
except IndexError as e:
    raise SystemExit(0) from e
