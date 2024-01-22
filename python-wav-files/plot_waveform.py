from argparse import ArgumentParser
from pathlib import Path

from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter

from waveio.reader import WaveReader


def main():
    args = parse_args()
    with WaveReader(args.path) as reader:
        plot(reader.channels_sliced(args.begin, args.end))


def parse_args():
    parser = ArgumentParser(
        description="Plot WAV file waveform",
        epilog="Example: plot_waveform.py sounds/Bongo_sound.wav -b -2.5",
    )
    parser.add_argument("path", type=Path, help="path to the WAV file")
    parser.add_argument(
        "-b",
        "--begin",
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


def plot(channels):
    try:
        plt.style.use("fivethirtyeight")
    except OSError:
        pass  # Fall back to the default style

    fig, ax = plt.subplots(
        nrows=len(channels),
        ncols=1,
        figsize=(16, 9),
        sharex=True,
    )

    if isinstance(ax, plt.Axes):
        ax = [ax]

    time_formatter = FuncFormatter(format_time)

    for i, channel in enumerate(channels):
        ax[i].plot(channels.x_range, channel)
        ax[i].set_title(f"Channel #{i + 1}")
        ax[i].set_yticks([-1, -0.5, 0, 0.5, 1])
        ax[i].xaxis.set_major_formatter(time_formatter)

    plt.tight_layout()
    plt.show()


def format_time(seconds, _):
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes:02}:{seconds:02}"


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Aborted")
