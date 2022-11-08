import argparse

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument("files", nargs="+")

args = arg_parser.parse_args()

print(args)
