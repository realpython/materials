# Python 3.15 Preview: Sampling Profiler

Supporting code for the Real Python tutorial [Python 3.15 Preview: Sampling Profiler](https://realpython.com/python315-sampling-profiler/).

Pretzel is a tiny 3D model viewer that spins a trefoil-knot pretzel in a Tkinter window. It ships with a few deliberately planted performance bottlenecks so that every feature of the new `profiling.sampling` profiler has something real to find:

- A **pure-Python hotspot** in the vertex transformation math (`engine.py`)
- A **native-code hotspot** in the NumPy-based lighting (`shading.py`)
- An **I/O-bound bottleneck** that flushes telemetry to disk on every frame (`telemetry.py`)
- A **wasteful asset parser** that reads wallpapers one byte at a time, both at startup and in a background thread (`assets.py` and `streaming.py`)

## Setup

Install [uv](https://docs.astral.sh/uv/), then create the virtual environment. Because `pyproject.toml` pins `requires-python = ">=3.15"`, uv downloads a pre-built CPython 3.15 pre-release for you if you don't have one yet:

```sh
$ uv sync
```

## Running the Viewer

Open the animation in a window:

```sh
$ uv run pretzel
```

Render a fixed number of frames without a window, which is handy for repeatable profiling runs:

```sh
$ uv run pretzel --frames 300
```

Both modes accept `--fast`, which switches to the optimized asset loader and buffered telemetry:

```sh
$ uv run pretzel --frames 300 --fast
```

You can also use `--cache-colors` to memoize the polygon color formatting in `render.py`. It's the in-place fix showcased by the tutorial's first differential flame graph:

```sh
$ uv run pretzel --frames 300 --cache-colors
```

## Profiling the Viewer

The commands below mirror the tutorial. Run them from this directory:

```sh
# Profile a complete headless run:
$ uv run python -m profiling.sampling run -m pretzel --frames 300

# Only count samples where the main thread runs on the CPU:
$ uv run python -m profiling.sampling run --mode cpu -m pretzel --frames 300

# Sample the background thread, too:
$ uv run python -m profiling.sampling run -a -m pretzel --frames 300

# Generate an interactive flame graph:
$ uv run python -m profiling.sampling run --flamegraph -o flamegraph.html \
    -m pretzel --frames 300

# Generate a line-level heatmap:
$ uv run python -m profiling.sampling run --heatmap -o heatmap \
    -m pretzel --frames 300

# Record a binary profile, then convert it later:
$ uv run python -m profiling.sampling run --binary -o slow.bin \
    -m pretzel --frames 300
$ uv run python -m profiling.sampling replay slow.bin

# Compare the in-place color-cache fix against the recorded baseline:
$ uv run python -m profiling.sampling run --diff-flamegraph slow.bin \
    -o diff-colors.html -m pretzel --frames 300 --cache-colors

# Compare the parser and telemetry fixes against the same baseline:
$ uv run python -m profiling.sampling run --diff-flamegraph slow.bin \
    -o diff.html -m pretzel --frames 300 --fast
```

To attach to a running viewer, start `uv run pretzel` in one terminal and run one of the following commands in another terminal. The attaching interpreter must be the same Python version as the target, which is why these commands point `sudo` at the interpreter inside `.venv`:

```sh
$ sudo .venv/bin/python -m profiling.sampling attach $(pgrep -n -f "pretzel$")
$ sudo .venv/bin/python -m profiling.sampling dump $(pgrep -n -f "pretzel$")
$ sudo .venv/bin/python -m profiling.sampling attach --live \
    $(pgrep -n -f "pretzel$")
```

## Profiling the Async Example

The `examples/fetch_textures.py` script simulates concurrent texture downloads:

```sh
$ uv run python -m profiling.sampling run --async-aware \
    examples/fetch_textures.py
$ uv run python -m profiling.sampling run --async-aware --async-mode all \
    examples/fetch_textures.py
```

## Regenerating the Assets

The model and wallpaper files under `src/pretzel/assets/` are checked in, but you can regenerate them at any time:

```sh
$ uv run make_assets.py
```

## About the .mdl Format

`pretzel.mdl` uses a minimal text format inspired by Wavefront OBJ: lines starting with `v` define `x y z` vertices, and lines starting with `f` define faces or triangles as 1-based vertex indices.
