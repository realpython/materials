# Claude Opus 5 Draws a Python Reading a Book

This folder holds the sample code for the Real Python write-up [Claude Opus 5 Draws a Python Reading a Book](https://realpython.com/ai-benchmark-claude-opus-5/), part of [How AI Models Draw a Python Reading a Book](https://realpython.com/ai-benchmark/).

- Model: `anthropic/claude-opus-5`, at its default reasoning settings, run on 2026-09-08
- Prompt: *Write a Python turtle program that draws a python reading a book.*

## What's Here

| File | What |
|---|---|
| `claude-opus-5-python-reading-a-book.py` | The turtle script, exactly as the model returned it, with a header naming the model, date, and prompt |
| `claude-opus-5-python-reading-a-book.png` | The finished drawing, rendered headlessly at 800×600 |
| `claude-opus-5-python-reading-a-book.gif` | The turtle drawing it, frame by frame |

## Run It

You need Python with `tkinter`, which ships with the standard installers from python.org:

```sh
$ python claude-opus-5-python-reading-a-book.py
```

A window opens and the turtle draws the picture. Change a color, a coordinate, or the caption and run it again to see what the model's code is actually doing. To learn the module from scratch, start with [The Beginner's Guide to Python's turtle Module](https://realpython.com/beginners-guide-python-turtle/).

## A Note on the Code

Nothing in the script was fixed up. It's the model's output verbatim, so it isn't formatted to this repository's Ruff rules on purpose. That's part of what the write-up reads off it.

When we ran it on Python 3.13, the script crashed partway through with `AttributeError: 'Turtle' object has no attribute 'settiltangle'`. That method was removed from the `turtle` module in Python 3.13, so the drawing stops after the books and the mug. That's also part of what the write-up reads off it.
