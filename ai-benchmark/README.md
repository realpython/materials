# How AI Models Draw a Python Reading a Book

Sample code for Real Python's [vibe check for new AI models](https://realpython.com/ai-benchmark/). Every new model gets the same fixed prompt, *Write a Python turtle program that draws a python reading a book*, and the result is published as is, drawing and all.

Each subfolder is one model's run, named after the model id without its vendor prefix. It contains the turtle script exactly as the model returned it, the rendered drawing, the animation of the turtle drawing it, and a README with the details of that run.

| Folder | Write-up |
|---|---|
| [`gpt-6-astra/`](gpt-6-astra/) | [GPT-6 Astra Draws a Python Reading a Book](https://realpython.com/ai-benchmark-gpt-6-astra/) |

The scripts are the models' output verbatim and are excluded from this repository's Ruff checks on purpose. Nothing was fixed up; that's the point.
