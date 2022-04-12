import sys

try:
    sys.exit(sys.argv[1])
except IndexError:
    sys.exit(0)
