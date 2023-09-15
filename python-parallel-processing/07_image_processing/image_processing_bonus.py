# image_processing.py

import argparse
import enum
import pathlib
import time
import tkinter as tk
import tkinter.ttk as ttk

import numpy as np
import PIL.Image
import PIL.ImageTk

import parallel


class ProcessingMode(enum.StrEnum):
    PYTHON = "Python"
    NUMPY = "NumPy"
    PARALLEL = "Parallel (GIL-Free)"


class AppWindow(tk.Tk):
    def __init__(self, image: PIL.Image.Image) -> None:
        super().__init__()

        # Main window
        self.title("Exposure and Gamma Correction")
        self.resizable(False, False)

        # Parameters frame
        self.frame = ttk.LabelFrame(self, text="Parameters")
        self.frame.pack(fill=tk.X, padx=10, pady=10)
        self.frame.columnconfigure(0, weight=0)
        self.frame.columnconfigure(1, weight=1)

        # Dropdown
        self.var_mode = tk.StringVar(value=ProcessingMode.PYTHON)
        mode_label = ttk.Label(self.frame, text="Mode:")
        mode_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
        mode_dropdown = ttk.Combobox(
            self.frame,
            textvariable=self.var_mode,
            values=list(ProcessingMode),
            state="readonly",
        )
        mode_dropdown.grid(
            row=0, column=1, sticky=tk.W + tk.E, padx=10, pady=10
        )

        # EV slider
        self.var_ev = tk.DoubleVar(value=0)
        ev_label = ttk.Label(self.frame, text="Exposure:")
        ev_label.grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)
        ev_slider = ttk.Scale(
            self.frame,
            from_=-1,
            to=1,
            orient=tk.HORIZONTAL,
            variable=self.var_ev,
        )
        ev_slider.bind("<B1-Motion>", self.on_slide)
        ev_slider.grid(row=1, column=1, sticky=tk.W + tk.E, padx=10, pady=10)

        # Gamma slider
        self.var_gamma = tk.DoubleVar(value=1)
        gamma_label = ttk.Label(self.frame, text="Gamma:")
        gamma_label.grid(row=2, column=0, sticky=tk.W, padx=10, pady=10)
        gamma_slider = ttk.Scale(
            self.frame,
            from_=0.1,
            to=2,
            orient=tk.HORIZONTAL,
            variable=self.var_gamma,
        )
        gamma_slider.bind("<B1-Motion>", self.on_slide)
        gamma_slider.grid(
            row=2, column=1, sticky=tk.W + tk.E, padx=10, pady=10
        )

        # Image preview
        self.preview = ttk.Label(self, relief=tk.SUNKEN)
        self.preview.pack(padx=10, pady=10)

        # Status bar
        self.var_status = tk.StringVar()
        status_bar = ttk.Label(
            self,
            anchor=tk.W,
            relief=tk.SUNKEN,
            textvariable=self.var_status,
        )
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Image pixels
        self.pixels = np.array(image)
        self.update()
        self.show_preview(image)

        self.mainloop()

    def on_slide(self, *args, **kwargs) -> None:
        # Get parameters
        ev = 2.0 ** self.var_ev.get()
        gamma = 1.0 / self.var_gamma.get()

        # Process pixels
        t1 = time.perf_counter()
        pixels = self.process(ev, gamma)
        t2 = time.perf_counter()

        # Render preview
        image = PIL.Image.fromarray(pixels)
        self.show_preview(image)
        t3 = time.perf_counter()

        # Update status
        self.var_status.set(
            f"Processed in {(t2 - t1) * 1000:.0f} ms "
            f"(Rendered in {(t3 - t1) * 1000:.0f} ms)"
        )

    def show_preview(self, image: PIL.Image.Image) -> None:
        scale = 0.75
        offset = 2.0 * self.frame.winfo_height()
        image.thumbnail(
            (
                int(self.winfo_screenwidth() * scale),
                int(self.winfo_screenheight() * scale - offset),
            )
        )
        image_tk = PIL.ImageTk.PhotoImage(image)
        self.preview.configure(image=image_tk)
        self.preview.image = image_tk

    def process(self, ev: float, gamma: float) -> np.ndarray:
        match mode := self.var_mode.get():
            case ProcessingMode.PYTHON:
                return process_python(self.pixels, ev, gamma)
            case ProcessingMode.NUMPY:
                return process_numpy(self.pixels, ev, gamma)
            case ProcessingMode.PARALLEL:
                parallel.process(pixels := self.pixels.copy(), ev, gamma)
                return pixels
            case _:
                raise ValueError(f"Invalid mode: {mode}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("image_path", type=pathlib.Path)
    return parser.parse_args()


def main(args: argparse.Namespace) -> None:
    with PIL.Image.open(args.image_path) as image:
        AppWindow(image)


def process_python(pixels: np.ndarray, ev: float, gamma: float) -> np.ndarray:
    lookup_table = [
        int(min(max(0, (((i / 255.0) * ev) ** gamma) * 255), 255))
        for i in range(256)
    ]
    values = [lookup_table[x] for x in pixels.flat]
    return np.array(values).astype(np.uint8).reshape(pixels.shape)


def process_numpy(pixels: np.ndarray, ev: float, gamma: float) -> np.ndarray:
    lookup_table = (
        ((((np.arange(256) / 255.0) * ev) ** gamma) * 255)
        .clip(0, 255)
        .astype(np.uint8)
    )
    return lookup_table[pixels]


if __name__ == "__main__":
    main(parse_args())
