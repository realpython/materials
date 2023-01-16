import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--size", choices=["S", "M", "L", "XL"], default="M")

args = arg_parser.parse_args()

print(args)
