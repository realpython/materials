import argparse
import itertools

MAX_BYTES = 1024


def main(args):
    buffer = bytearray()
    with open(args.path, mode="rb") as file:
        while chunk := file.read(MAX_BYTES):
            buffer.extend(chunk)
    for row in itertools.batched(buffer, args.columns):
        print(" ".join(f"{byte:02x}" for byte in row))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("-c", "--columns", type=int, default=16)
    return parser.parse_args()


if __name__ == "__main__":
    main(parse_args())
