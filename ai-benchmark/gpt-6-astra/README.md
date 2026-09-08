# GPT-6 Astra Draws a Python Reading a Book

This folder holds the sample code for the Real Python write-up [GPT-6 Astra Draws a Python Reading a Book](https://realpython.com/ai-benchmark-gpt-6-astra/), part of [How AI Models Draw a Python Reading a Book](https://realpython.com/ai-benchmark/).

- Model: `openai/gpt-6-astra`, at its default reasoning settings, run on 2026-09-04
- Prompt: *Write a Python turtle program that draws a python reading a book.*

## What's Here

| File | What |
|---|---|
| `gpt-6-astra-python-reading-a-book.py` | The turtle script, exactly as the model returned it, with a header naming the model, date, and prompt |
| `gpt-6-astra-python-reading-a-book.png` | The finished drawing, rendered headlessly at 800×600 |
| `gpt-6-astra-python-reading-a-book.gif` | The turtle drawing it, frame by frame |

## Run It

You need Python with `tkinter`, which ships with the standard installers from python.org:

```sh
$ python gpt-6-astra-python-reading-a-book.py
```

A window opens and the turtle draws the picture. Change a color, a coordinate, or the caption and run it again to see what the model's code is actually doing. To learn the module from scratch, start with [The Beginner's Guide to Python's turtle Module](https://realpython.com/beginners-guide-python-turtle/).

## A Note on the Code

Nothing in the script was fixed up. It's the model's output verbatim, so it isn't formatted to this repository's Ruff rules on purpose. That's part of what the write-up reads off it.
