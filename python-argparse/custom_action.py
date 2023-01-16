import argparse


class VerboseStore(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print(f"Storing {values} in the {option_string} option...")
        setattr(namespace, self.dest, values)


arg_parser = argparse.ArgumentParser()

arg_parser.add_argument("-n", "--name", action=VerboseStore)

args = arg_parser.parse_args()

print(args)
