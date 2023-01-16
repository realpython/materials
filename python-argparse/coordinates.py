import argparse

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument(
    "--coordinates",
    nargs=2,
    metavar=("X", "Y"),
    help="take the Cartesian coordinates %(metavar)s",
)

args = arg_parser.parse_args()

print(args)
