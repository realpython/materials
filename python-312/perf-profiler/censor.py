import sys
from argparse import ArgumentParser


def main(args):
    censorship = censor(args.modules)
    for line in sys.stdin:
        stack_trace, num_samples = line.rsplit(maxsplit=1)
        symbols = filter(censorship, stack_trace.split(";"))
        censored_stack_trace = ";".join(symbols)
        if censored_stack_trace:
            print(censored_stack_trace, num_samples)


def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        "-m", "--modules", default=[], type=lambda s: s.split(",")
    )
    return parser.parse_args()


def censor(modules):
    def is_valid(symbol):
        if not symbol.startswith("py::"):
            return False
        if modules:
            return any(module in symbol for module in modules)
        return True

    return is_valid


if __name__ == "__main__":
    main(parse_args())
