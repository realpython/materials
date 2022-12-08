import argparse

parser = argparse.ArgumentParser()

parser.add_argument("numbers", nargs="*", type=float)

args = parser.parse_args()

print(sum(args.numbers))
