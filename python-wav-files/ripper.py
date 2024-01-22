from argparse import ArgumentParser

from radio import RadioStream
from waveio.writer import WaveWriter


def main():
    args = parse_args()
    with RadioStream(args.stream_url) as stream:
        with WaveWriter(stream.metadata, args.output) as writer:
            for chunk in stream:
                writer.append_bytes(chunk)


def parse_args():
    parser = ArgumentParser(
        description="Record an Internet radio stream",
        epilog="Example: ripper.py http://prem2.di.fm/lounge -o output.wav",
    )
    parser.add_argument("stream_url", help="URL address of the stream")
    parser.add_argument(
        "-o",
        "--output",
        metavar="path",
        required=True,
        type=str,
        help="path to the output WAV file",
    )
    return parser.parse_args()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Aborted")
