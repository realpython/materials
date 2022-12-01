import argparse

arg_parser = argparse.ArgumentParser(fromfile_prefix_chars="@")

arg_parser.add_argument("one")
arg_parser.add_argument("two")
arg_parser.add_argument("three")

args = arg_parser.parse_args()

print(args)
