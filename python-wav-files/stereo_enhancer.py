from argparse import ArgumentParser

from waveio.reader import WaveReader
from waveio.writer import WaveWriter


def main():
    args = parse_args()
    with (
        WaveReader(args.input_path) as reader,
        WaveWriter(reader.metadata, args.output_path) as writer,
    ):
        if reader.stereo:
            for left, right in reader.channels_lazy():
                middle = (left + right) / 2
                writer.append_channels(
                    left - middle * args.strength,
                    right - middle * args.strength,
                )
        else:
            print("Only stereo WAV files supported")


def parse_args():
    parser = ArgumentParser(
        description="Enhance stereo separation",
        epilog="Example: stereo_enhancer.py -i in.wav -o out.wav -s 0.5",
    )
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
        default=1,
        help="strength (defaults to 1)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Aborted")
