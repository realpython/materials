import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "--coordinates",
    nargs=2,
    metavar=("X", "Y"),
    help="take the Cartesian coordinates %(metavar)s",
)

args = parser.parse_args()

print(args)
