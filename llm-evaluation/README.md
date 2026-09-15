# LLM Evaluation in Python: Build an Eval Harness From Scratch

This folder contains the source code for [LLM Evaluation in Python: Build an Eval Harness From Scratch](https://realpython.com/llm-evaluation/).

- `follow_along/` contains the prompts, replay corpus, and setup files that you should start with.
- `completed/` contains the finished evaluation harness.

## Setup

Move into `follow_along/`, then create your virtual environment and install the dependencies:

```console
$ uv sync
```

## Usage

Replay mode is the default and needs no API key, since every command reads recorded generations and judgments from `data/replay/`:

```console
$ uv run evals.py run --prompt prompts/support_v1.txt
```

Live mode calls the OpenAI API through the same `ModelClient` protocol. Copy `.env.example` to `.env`, add your key, then pass `--live`.

See the tutorial for the full walkthrough.
