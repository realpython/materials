# Prompt Engineering: A Practical Example

This folder contains the code for the Real Python tutorial on [practical prompt engineering](https://realpython.com/practical-prompt-engineering/).

The project classifies synthetic customer support conversations with OpenAI's Responses API. You define a follow-up policy, write a prompt for it, and compare prompts against labeled cases so that you can tell whether a change helped.

## Setup

Export your OpenAI API key as an environment variable:

```bash
$ export OPENAI_API_KEY="your-api-key"
```

You can generate your [API key](https://platform.openai.com/api-keys) in your OpenAI account settings. API calls cost money, and each conversation you evaluate makes a separate request. Check the [API pricing](https://developers.openai.com/api/docs/pricing) before running a larger dataset.

## Install

Create and activate a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/). Then install the dependencies:

```bash
(venv) $ python -m pip install -r requirements.txt
```

The examples were tested with Python 3.14.7.

## Usage

Run one conversation through the baseline prompt:

```bash
(venv) $ python try_prompt.py
```

Evaluate a prompt against the six development cases:

```bash
(venv) $ python evaluate.py baseline.txt
(venv) $ python evaluate.py policy.txt
(venv) $ python evaluate.py examples.txt
```

Once you've chosen a prompt, check it against the four held-out cases:

```bash
(venv) $ python evaluate_test.py policy.txt
```

Each run prints the label matches, the exact-quote checks, the number of failed requests with the reason for each, and the model that answered.

## Files

The folder contains the following files:

- [LICENSE](LICENSE): License information
- [README.md](README.md): Information on the project and how to use it
- [baseline.txt](baseline.txt): Short zero-shot prompt that leaves the policy unstated
- [cases.py](cases.py): Development and held-out conversations with their expected labels
- [classify.py](classify.py): Model call, result schema, and error handling
- [evaluate.py](evaluate.py): Scores a prompt against the development cases
- [evaluate_test.py](evaluate_test.py): Scores a prompt against the held-out cases
- [examples.txt](examples.txt): The policy prompt plus two few-shot examples
- [policy.txt](policy.txt): Prompt that states the decision rules explicitly
- [requirements.txt](requirements.txt): Project requirements
- [try_prompt.py](try_prompt.py): Runs a prompt on a single conversation

You can find more information about when and how to use the different files [in the tutorial](https://realpython.com/practical-prompt-engineering/).

## Choosing a Model

`classify.py` sets `MODEL = "gpt-5.6-luna"`, a cost-optimized model that supports structured output. To run the examples on OpenAI's most capable model instead, set `MODEL = "gpt-6-astra"`. The techniques are identical, but each request costs considerably more.

Model availability changes over time. Check the [model documentation](https://developers.openai.com/api/docs/models) and the [deprecations page](https://developers.openai.com/api/docs/deprecations) to confirm that your chosen model is still available.

Both model names are aliases, and OpenAI can point an alias at a new version. Where a dated snapshot exists for your model, prefer it for comparisons that you'll rerun over days or weeks. That's why the evaluation scripts record which model answered each request.

## Prompts

The tutorial builds up three prompts, each in its own file so that you can track changes with version control:

1. [`baseline.txt`](baseline.txt): Describes the task without stating the policy
2. [`policy.txt`](policy.txt): Adds the numbered decision rules
3. [`examples.txt`](examples.txt): Adds two few-shot examples to the policy

Change one part of the experiment at a time and rerun the evaluation, so that you can tell what caused a difference in the results.

## About the Data

All conversations in `cases.py` are synthetic. The scripts produce suggestions for review; they don't contact customers or close tickets. Keep real customer information out of your experiments unless you're authorized to send it to your chosen service.

## License

Distributed under the MIT license. See `LICENSE` for more information.
