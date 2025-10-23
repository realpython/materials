import argparse

parser = argparse.ArgumentParser("Command-Line Interface")
parser.add_argument("path", help="Path to a file")
parser.parse_args()
