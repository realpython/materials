"""
Command line arguments parsing.
"""

import argparse
import pathlib
from dataclasses import dataclass
from typing import Optional


@dataclass
class CommandLineArguments:
    """Parsed command line arguments."""

    bitmap: pathlib.Path
    encode: Optional[pathlib.Path]
    decode: bool
    erase: bool


def parse_args() -> CommandLineArguments:
    """Parse command line arguments."""

    parser = argparse.ArgumentParser()
    parser.add_argument("bitmap", type=path_factory)

    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--encode", "-e", metavar="file", type=path_factory)
    modes.add_argument("--decode", "-d", action="store_true")
    modes.add_argument("--erase", "-x", action="store_true")

    args = parser.parse_args()

    if not any([args.encode, args.decode, args.erase]):
        parser.error("Mode required: --encode file | --decode | --erase")

    return CommandLineArguments(**vars(args))


def path_factory(argument: str) -> pathlib.Path:
    """Convert the argument to a path instance."""

    path = pathlib.Path(argument)

    if not path.exists():
        raise argparse.ArgumentTypeError("file doesn't exist")

    if not path.is_file():
        raise argparse.ArgumentTypeError("must be a file")

    return path
