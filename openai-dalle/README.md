# Generate Images With DALL·E and the OpenAI API

Learn to use the OpenAI Python library to create images with DALL·E, a state-of-the-art latent diffusion model. In the associated tutorial on [generating images with DALL·E and the OpenAI API](https://realpython.com/generate-images-with-dalle-openai-api/), you'll explore image creation and generating image variations. You'll learn how to interact with DALL·E using API calls and incorporate this functionality into your Python scripts.

## Setup

Create and activate a virtual environment, then install the `openai` package:

```console
$ python --version
Python 3.12.5
$ python -m venv venv
$ source venv/bin/activate
(venv) $ python -m pip install openai
```

You need to be on Python 3.7.1 or higher.

## Create Images and Image Variations

Follow the instructions in [the tutorial](https://realpython.com/generate-images-with-dalle-openai-api/) to create images from text prompts, create image variations, and convert a Base64 JSON response to a PNG image file.

You can find the code for each of these steps in dedicated scripts:

- `create_dalle3.py`: Create an image from a text prompt using DALL·E 3 and display the URL to the image.
- `create.py`: Create an image from a text prompt using DALL·E 2 and save the image data to a file.
- `convert.py`: Convert a Base64-encoded PNG image delivered in a JSON response to a PNG image file.
- `vary.py`: Read Base64-encoded image data and make an API request to receive variations of that image.

In the tutorial, you'll walk through each of these scripts and their functionality and output in more detail.

## Edit Images (Inpainting and Outpainting)

The OpenAI Image API also allows you to [edit parts of an image](https://platform.openai.com/docs/guides/images/edits-dall-e-2-only) using text prompts. For this, you need to create a mask with transparent image data in the area where you want to edit the image.

You can run `edit.py` to give this functionality a try.
