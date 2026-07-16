"""Tkinter front end that animates the model in a window."""

import time
import tkinter as tk
from typing import Final

from pretzel.engine import Mesh
from pretzel.render import compute_frame
from pretzel.streaming import BackgroundStreamer
from pretzel.telemetry import FrameLog

WIDTH: Final = 512
HEIGHT: Final = 512


class Viewer:
    def __init__(
        self,
        mesh: Mesh,
        streamer: BackgroundStreamer,
        frame_log: FrameLog,
    ) -> None:
        self.mesh = mesh
        self.streamer = streamer
        self.frame_log = frame_log
        self.frame = 0
        self.started = time.perf_counter()
        self.window = tk.Tk()
        self.window.title("Pretzel")
        self.window.resizable(False, False)
        self.canvas = tk.Canvas(
            self.window, width=WIDTH, height=HEIGHT, highlightthickness=0
        )
        self.canvas.pack()
        self.wallpaper = tk.PhotoImage(file=streamer.background.path)
        self.backdrop = self.canvas.create_image(
            0, 0, image=self.wallpaper, anchor=tk.NW
        )

    def run(self) -> None:
        self.window.after(1, self.render_next_frame)
        self.window.mainloop()

    def render_next_frame(self) -> None:
        frame_started = time.perf_counter()
        background = self.streamer.background
        if background.path != str(self.wallpaper.cget("file")):
            self.wallpaper.configure(file=background.path)
        tick = frame_started - self.started
        polygons = compute_frame(self.mesh, background, tick, WIDTH, HEIGHT)
        self.canvas.delete("model")
        for coordinates, color in polygons:
            self.canvas.create_polygon(
                coordinates, fill=color, outline="", tags="model"
            )
        elapsed_ms = (time.perf_counter() - frame_started) * 1000
        self.frame_log.record(self.frame, elapsed_ms)
        self.frame += 1
        self.window.title(f"Pretzel ({1000 / elapsed_ms:.0f} fps)")
        self.window.after(1, self.render_next_frame)
