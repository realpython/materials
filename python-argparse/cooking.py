import argparse

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument("--veggies", nargs="+")
arg_parser.add_argument("--fruits", nargs="*")

args = arg_parser.parse_args()

print(args)
