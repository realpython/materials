import argparse

parser = argparse.ArgumentParser(fromfile_prefix_chars="@")

parser.add_argument("one")
parser.add_argument("two")
parser.add_argument("three")

args = parser.parse_args()

print(args)
