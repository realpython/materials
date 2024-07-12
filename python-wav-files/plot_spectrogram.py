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
            args.overlap,
            fft(slide_window(args.seconds, args.overlap, wav), wav),
        )


def parse_args():
    parser = ArgumentParser(description="Animate WAV file spectrogram")
    parser.add_argument("path", type=Path, help="path to the WAV file")
    parser.add_argument(
        "-s",
        "--seconds",
        type=float,
        default=0.0015,
        help="sliding window size in seconds",
    )
    parser.add_argument(
        "-o",
        "--overlap",
        choices=range(100),
        default=50,
        type=int,
        help="sliding window overlap as a percentage",
    )
    return parser.parse_args()


def slide_window(window_seconds, overlap_percentage, wav):
    step_seconds = window_seconds * (1 - overlap_percentage / 100)
    num_windows = round(wav.metadata.num_seconds / step_seconds)
    for i in range(num_windows):
        begin_seconds = i * step_seconds
        end_seconds = begin_seconds + window_seconds
        channels = wav.channels_sliced(begin_seconds, end_seconds)
        yield np.mean(tuple(channels), axis=0)


def fft(windows, wav):
    sampling_period = 1 / wav.metadata.frames_per_second
    for window in windows:
        frequencies = np.fft.rfftfreq(window.size, sampling_period)
        magnitudes = np.abs(
            np.fft.rfft((window - np.mean(window)) * np.blackman(window.size))
        )
        yield frequencies, magnitudes


def animate(filename, seconds, overlap_percentage, windows):
    try:
        plt.style.use("dark_background")
    except OSError:
        pass  # Fall back to the default style

    fig, ax = plt.subplots(figsize=(16, 9))
    fig.canvas.manager.set_window_title(filename)

    plt.tight_layout()
    plt.box(False)

    bar_gap = 0.25
    for frequencies, magnitudes in windows:
        bar_width = (frequencies[-1] / frequencies.size) * (1 - bar_gap)
        plt.cla()
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlim(-bar_width / 2, frequencies[-1] - bar_width / 2)
        ax.set_ylim(0, np.max(magnitudes))
        ax.bar(frequencies, magnitudes, width=bar_width)
        plt.pause(seconds * (1 - overlap_percentage / 100))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Aborted")
