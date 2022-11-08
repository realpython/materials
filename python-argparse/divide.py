import argparse

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument("--dividend", type=float)
arg_parser.add_argument("--divisor", type=float)

args = arg_parser.parse_args()

print(args.dividend / args.divisor)
