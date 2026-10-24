import argparse

parser = argparse.ArgumentParser()

parser.add_argument("files", nargs="+")

args = parser.parse_args()

print(args)
