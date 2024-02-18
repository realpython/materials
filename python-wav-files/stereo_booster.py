from argparse import ArgumentParser

from waveio import WAVReader, WAVWriter


def main():
    args = parse_args()
    with (
        WAVReader(args.input_path) as source,
        WAVWriter(source.metadata, args.output_path) as target,
    ):
        if source.stereo:
            for channels_chunk in source.channels_lazy():
                mid, side = convert_to_ms(*channels_chunk)
                left, right = convert_to_lr(mid, side * args.strength)
                target.append_channels(left, right)
        else:
            print("Only stereo WAV files are supported")


def convert_to_ms(left, right):
    return (left + right) / 2, (left - right) / 2


def convert_to_lr(mid, side):
    return mid + side, mid - side


def parse_args():
    parser = ArgumentParser(description="Widen the stereo field")
    parser.add_argument(
        "-i",
        "--input",
        dest="input_path",
        required=True,
        type=str,
        help="path to the input WAV file",
    )
    parser.add_argument(
        "-o",
        "--output",
        dest="output_path",
        required=True,
        type=str,
        help="path to the output WAV file",
    )
    parser.add_argument(
        "-s",
        "--strength",
        type=float,
        default=1.0,
        help="strength (defaults to 1)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Aborted")
