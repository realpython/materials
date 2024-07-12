from argparse import ArgumentParser

from stream import RadioStream
from waveio import WAVWriter


def main():
    args = parse_args()
    with RadioStream(args.stream_url) as radio_stream:
        with WAVWriter(radio_stream.metadata, args.output) as writer:
            for channels_chunk in radio_stream:
                writer.append_channels(channels_chunk)


def parse_args():
    parser = ArgumentParser(description="Record an Internet radio stream")
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
