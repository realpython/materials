import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--size", choices=["S", "M", "L", "XL"], default="M")

args = parser.parse_args()

print(args)
