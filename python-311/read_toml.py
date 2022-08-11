import sys
from pprint import pp

try:
    import tomllib
except ImportError:
    import tomli as tomllib

for filename in sys.argv[1:]:
    print(filename.center(60, "="))
    with open(filename, mode="rb") as fp:
        pp(tomllib.load(fp))
