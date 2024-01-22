from argparse import ArgumentParser
from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt

from waveio.reader import WaveReader

type Samples = np.ndarray


def main():
    args = parse_args()
    with WaveReader(args.path) as reader:
        animate(args.seconds, slide_window(args.seconds, reader))


def parse_args():
    parser = ArgumentParser(
        description="Animate WAV file waveform",
        epilog="Example: oscilloscope.py sounds/Bongo_sound.wav -s 0.1",
    )
    parser.add_argument("path", type=Path, help="path to the WAV file")
    parser.add_argument(
        "-s",
        "--seconds",
        type=float,
        default=0.01,
        help="size of the sliding window in seconds",
    )
    return parser.parse_args()


def slide_window(seconds, reader):
    num_windows = round(reader.metadata.num_seconds / seconds)
    for i in range(num_windows):
        begin_seconds = i * seconds
        end_seconds = begin_seconds + seconds
        channels = reader.channels_sliced(begin_seconds, end_seconds)
        yield np.mean(tuple(channels), axis=0)


def animate(seconds, slider):
    try:
        plt.style.use("dark_background")
    except OSError:
        pass  # Fall back to the default style

    fig, ax = plt.subplots(figsize=(16, 9))

    plt.tight_layout()
    plt.box(False)

    for window in slider:
        plt.cla()
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_ylim(-1.0, 1.0)
        plt.plot(window)
        plt.pause(seconds)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Aborted")
