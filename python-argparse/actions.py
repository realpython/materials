import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "--name", action="store"
)  # Equivalent to arg_parser.add_argument("--name")
parser.add_argument("--pi", action="store_const", const=3.14)
parser.add_argument("--is-valid", action="store_true")
parser.add_argument("--is-invalid", action="store_false")
parser.add_argument("--item", action="append")
parser.add_argument("--repeated", action="append_const", const=42)
parser.add_argument("--add-one", action="count")
parser.add_argument("--version", action="version", version="%(prog)s 0.1.0")


args = parser.parse_args()

print(args)
