from argparse import ArgumentParser
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from waveio import WAVReader


def main():
    args = parse_args()
    with WAVReader(args.path) as wav:
        animate(
            args.path.name,
            args.seconds,
            slide_window(args.seconds, wav),
        )


def parse_args():
    parser = ArgumentParser(description="Animate WAV file waveform")
    parser.add_argument("path", type=Path, help="path to the WAV file")
    parser.add_argument(
        "-s",
        "--seconds",
        type=float,
        default=0.05,
        help="sliding window size in seconds",
    )
    return parser.parse_args()


def slide_window(window_seconds, wav):
    num_windows = round(wav.metadata.num_seconds / window_seconds)
    for i in range(num_windows):
        begin_seconds = i * window_seconds
        end_seconds = begin_seconds + window_seconds
        channels = wav.channels_sliced(begin_seconds, end_seconds)
        yield np.mean(tuple(channels), axis=0)


def animate(filename, seconds, windows):
    try:
        plt.style.use("dark_background")
    except OSError:
        pass  # Fall back to the default style

    fig, ax = plt.subplots(figsize=(16, 9))
    fig.canvas.manager.set_window_title(filename)

    plt.tight_layout()
    plt.box(False)

    for window in windows:
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
