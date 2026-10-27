import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--veggies", nargs="+")
parser.add_argument("--fruits", nargs="*")

args = parser.parse_args()

print(args)
