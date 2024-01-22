from argparse import ArgumentParser
from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt

from waveio.reader import WaveReader

type Samples = np.ndarray


def main():
    args = parse_args()
    with WaveReader(args.path) as reader:
        animate(
            args.seconds,
            reader.metadata.frames_per_second,
            slide_window(args.seconds, reader),
        )


def parse_args():
    parser = ArgumentParser(
        description="Animate WAV file spectrogram",
        epilog="Example: spectrogram.py sounds/Bongo_sound.wav -s 0.0025",
    )
    parser.add_argument("path", type=Path, help="path to the WAV file")
    parser.add_argument(
        "-s",
        "--seconds",
        type=float,
        default=0.001,
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


def animate(seconds, frames_per_second, slider):
    try:
        plt.style.use("dark_background")
    except OSError:
        pass  # Fall back to the default style

    fig, ax = plt.subplots(figsize=(16, 9))

    plt.tight_layout()
    plt.box(False)

    for window in slider:
        frequencies, magnitudes = fft(frames_per_second, window)
        frequency_bin_width = frequencies[1] - frequencies[0]

        plt.cla()
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_ylim(0, 0.0025)  # FIXME: Calculate or pass via CLI
        plt.bar(
            frequencies,
            magnitudes,
            width=frequency_bin_width,
            edgecolor="white",
        )
        plt.pause(seconds)


def fft(frames_per_second, samples):
    sampling_period = 1.0 / frames_per_second
    frequencies = np.fft.rfftfreq(len(samples), d=sampling_period)
    magnitudes = np.abs(np.fft.rfft(samples, norm="forward"))
    return frequencies, magnitudes


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Aborted")
