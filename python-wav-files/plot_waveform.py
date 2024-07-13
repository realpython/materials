from argparse import ArgumentParser
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
from waveio import WAVReader


def main():
    args = parse_args()
    with WAVReader(args.path) as wav:
        plot(
            args.path.name,
            wav.metadata,
            wav.channels_sliced(args.start, args.end),
        )


def parse_args():
    parser = ArgumentParser(description="Plot the waveform of a WAV file")
    parser.add_argument("path", type=Path, help="path to the WAV file")
    parser.add_argument(
        "-s",
        "--start",
        type=float,
        default=0.0,
        help="start time in seconds (default: 0.0)",
    )
    parser.add_argument(
        "-e",
        "--end",
        type=float,
        default=None,
        help="end time in seconds (default: end of file)",
    )
    return parser.parse_args()


def plot(filename, metadata, channels):
    try:
        plt.style.use("fivethirtyeight")
    except OSError:
        pass  # Fall back to the default style

    fig, ax = plt.subplots(
        nrows=metadata.num_channels,
        ncols=1,
        figsize=(16, 9),
        sharex=True,
    )

    if isinstance(ax, plt.Axes):
        ax = [ax]

    time_formatter = FuncFormatter(format_time)
    timeline = np.linspace(
        channels.frames_range.start / metadata.frames_per_second,
        channels.frames_range.stop / metadata.frames_per_second,
        len(channels.frames_range),
    )

    for i, channel in enumerate(channels):
        ax[i].set_title(f"Channel #{i + 1}")
        ax[i].set_yticks([-1, -0.5, 0, 0.5, 1])
        ax[i].xaxis.set_major_formatter(time_formatter)
        ax[i].plot(timeline, channel)

    fig.canvas.manager.set_window_title(filename)
    plt.tight_layout()
    plt.show()


def format_time(instant, _):
    if instant < 60:
        return f"{instant:g}s"
    minutes, seconds = divmod(instant, 60)
    return f"{minutes:g}m {seconds:02g}s"


if __name__ == "__main__":
    main()
