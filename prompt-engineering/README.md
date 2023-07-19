# Practical Prompt Engineering

This repository contains a practical example to showcase a few common prompt engineering techniques. It's the code base used in the [associated Real Python tutorial on prompt engineering](https://realpython.com/practical-prompt-engineering/). The project allows you to preprocess customer service chats using GPT-3 and GPT-4 using the OpenAI API.

## Setup

Export your OpenAI API key as an environment variable:

```
export OPENAI_API_KEY="your-api-key"
```

You can generate your [API key](https://platform.openai.com/account/api-keys) in your OpenAI account settings.

## Install

Create and activate a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/). Then install the `openai` dependency:

```bash
(venv) $ python -m pip install openai
```

## Usage

Read support chat conversations from a file, sanitize the text, classify by sentiment, and format the output as JSON:

```bash
(venv) $ python app.py testing.txt
```

You can provide a different file as input file.

## Prompts And Output

Change the prompts used in the script by editing the entries in `settings.toml`.

In the tutorial, you learn how developing the prompt can give you better results based on a couple of prompting techniques.
