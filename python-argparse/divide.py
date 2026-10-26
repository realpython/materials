import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--dividend", type=int)
parser.add_argument("--divisor", type=int)

args = parser.parse_args()

print(args.dividend / args.divisor)
