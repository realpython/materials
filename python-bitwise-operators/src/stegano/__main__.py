"""
Runnable module, can be executed as:
$ python -m stegano
"""

from stegano.bitmap import Bitmap
from stegano.cli import CommandLineArguments, parse_args
from stegano.decoder import DecodingError, decode
from stegano.encoder import EncodingError, encode
from stegano.eraser import erase


def entry_point() -> None:
    """Entry point to the script."""
    try:
        main(parse_args())
    except (EncodingError, DecodingError) as ex:
        print(ex)


def main(args: CommandLineArguments) -> None:
    """Handle the command line arguments and perform actions."""
    with Bitmap(args.bitmap) as bitmap:
        if args.encode:
            encode(bitmap, args.encode)
        elif args.decode:
            decode(bitmap)
        elif args.erase:
            erase(bitmap)


if __name__ == "__main__":
    entry_point()
