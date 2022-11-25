import sys

print(sys.argv)

try:
    raise SystemExit(int(sys.argv[1]))
except IndexError as e:
    raise SystemExit(0) from e
except ValueError as e:
    print("Argument must be an integer")
    raise SystemExit() from e
