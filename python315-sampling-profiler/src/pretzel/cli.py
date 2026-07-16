"""Command-line entry point for the Pretzel viewer."""

import argparse
import time

from pretzel import assets
from pretzel.render import compute_frame
from pretzel.streaming import BackgroundStreamer
from pretzel.telemetry import FrameLog

MODEL = "pretzel.mdl"


def main():
    parser = argparse.ArgumentParser(prog="pretzel", description=__doc__)
    parser.add_argument(
        "--frames",
        metavar="N",
        type=int,
        default=None,
        help="render N frames headlessly instead of opening a window",
    )
    parser.add_argument(
        "--fast",
        action="store_true",
        help="use the optimized asset loader and buffered telemetry",
    )
    parser.add_argument(
        "--cache-colors",
        action="store_true",
        help="memoize polygon color formatting in headless mode",
    )
    args = parser.parse_args()

    mesh = assets.load_mesh(MODEL)
    streamer = BackgroundStreamer(fast=args.fast)
    streamer.start()
    frame_log = FrameLog("telemetry.csv", durable=not args.fast)
    try:
        if args.frames is None:
            show_window(mesh, streamer, frame_log)
        else:
            render_headlessly(
                mesh, streamer, frame_log, args.frames, args.cache_colors
            )
    finally:
        frame_log.close()


def show_window(mesh, streamer, frame_log):
    from pretzel.viewer import Viewer

    Viewer(mesh, streamer, frame_log).run()


def render_headlessly(
    mesh, streamer, frame_log, frames, cache_colors=False, size=512
):
    started = time.perf_counter()
    for frame in range(frames):
        frame_started = time.perf_counter()
        tick = frame_started - started
        compute_frame(
            mesh, streamer.background, tick, size, size, cache_colors
        )
        elapsed_ms = (time.perf_counter() - frame_started) * 1000
        frame_log.record(frame, elapsed_ms)
    total = time.perf_counter() - started
    print(
        f"Rendered {frames} frames in {total:.2f}s ({frames / total:.1f} fps)"
    )
