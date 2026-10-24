import argparse

my_parser = argparse.ArgumentParser()

my_parser.add_argument("--weekday", type=int, choices=range(1, 8))

args = my_parser.parse_args()

print(args)
