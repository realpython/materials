# How to Generate Images With the OpenAI API

Learn to use the OpenAI Python library to create images with the GPT Image models. In the associated tutorial on [generating images with the OpenAI API](https://realpython.com/generate-images-openai/), you'll create images from text prompts, tune the size and quality of your results, and edit an image with a follow-up prompt. You'll learn how to interact with the Images API and incorporate this functionality into your Python scripts.

## Setup

Create and activate a virtual environment, then install the `openai` package:

```console
$ python --version
Python 3.14.6
$ python -m venv venv
$ source venv/bin/activate
(venv) $ python -m pip install openai
```

You need to be on Python 3.10 or higher.

The scripts read your API key from the `OPENAI_API_KEY` environment variable:

```console
(venv) $ export OPENAI_API_KEY="<your-key-value-here>"
```

## Create and Edit Images

Follow the instructions in [the tutorial](https://realpython.com/generate-images-openai/) to create images from text prompts, edit an image with a follow-up prompt, and convert a Base64 JSON response to a PNG image file.

You can find the code for each of these steps in dedicated scripts:

- `create_png.py`: Create an image from a text prompt and write it straight to a PNG file.
- `create.py`: Create an image from a text prompt and save the whole JSON response to a file.
- `convert.py`: Convert a Base64-encoded PNG image delivered in a JSON response to a PNG image file.
- `edit.py`: Read Base64-encoded image data and make an API request to edit that image with a prompt.

In the tutorial, you'll walk through each of these scripts and their functionality and output in more detail.

Note that `convert.py` and `edit.py` read a saved response from the `responses/` directory. Run `create.py` first, then update the `JSON_FILE` and `SOURCE_FILE` constants to match the filename that it wrote.

## A Note on Models

The GPT Image models replaced DALL·E, which OpenAI [retired on May 12, 2026](https://developers.openai.com/api/docs/deprecations) along with the image variations endpoint. These scripts call `gpt-image-2`.

OpenAI retires image models on a regular schedule, so if a script starts failing with a message like `The model 'gpt-image-2' does not exist`, then check the deprecations page and swap the model name.
