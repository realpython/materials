import argparse

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument("--vegies", nargs="+")
arg_parser.add_argument("--fruits", nargs="*")

args = arg_parser.parse_args()

print(args)
