# Spec-Driven Development With AI: A Hands-on OpenSpec Guide

This folder contains the example project for the Real Python tutorial [Spec-Driven Development With AI: A Hands-on OpenSpec Guide](https://realpython.com/sdd-openspec/).

`habits` is a tiny command-line habit tracker written in pure Python. You'll use it to practice the propose, review, apply, and archive loop with [OpenSpec](https://github.com/Fission-AI/OpenSpec).

## Contents

- `source_code_initial/`: The starter project you begin the tutorial with, before OpenSpec is installed.
- `source_code_final/`: The finished project after both changes from the tutorial, including:
    - `openspec/specs/`: The two specs, `habit-stats` and `habit-check-in`, that the tutorial builds up
    - `openspec/changes/archive/`: The archived changes, `add-stats-command` and `backdate-check-ins`, with their proposals, spec deltas, designs, and task lists
    - `openspec/config.yaml`: The project context and rules added during the first review
    - `.claude/`: The slash commands and skills that `openspec init --tools claude` generated

## Setup

You'll need Python 3.12 or newer and [uv](https://docs.astral.sh/uv/). Run the app and its tests from either project folder:

```sh
$ cd source_code_initial/
$ export HABITS_FILE=/tmp/habits.json
$ uv run habits add read
$ uv run habits done read
$ uv run habits list
$ uv run --group dev pytest -q
```

To follow along with the spec-driven workflow, you'll also need [Node.js](https://nodejs.org/) 20.19.0 or newer and OpenSpec. The tutorial uses version 1.14.1:

```sh
$ npm install -g @fission-ai/openspec@1.14.1
$ openspec init --tools claude
```

Replace `claude` with the assistant you use, or leave out `--tools` to pick one from a menu. Run `openspec --help` for all options.
