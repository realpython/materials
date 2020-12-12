"""
Runnable module, can be executed as:
$ python -m stegano
"""

from .bitmap import Bitmap
from .cli import CommandLineArguments, parse_args
from .decoder import decode, DecodingError
from .encoder import encode, EncodingError
from .eraser import erase


def main(args: CommandLineArguments) -> None:
    """Entry point to the script."""
    with Bitmap(args.bitmap) as bitmap:
        if args.encode:
            encode(bitmap, args.encode)
        elif args.decode:
            decode(bitmap)
        elif args.erase:
            erase(bitmap)


if __name__ == "__main__":
    try:
        main(parse_args())
    except (EncodingError, DecodingError) as ex:
        print(ex)
