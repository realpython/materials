# Hugging Face Transformers: Leverage Open-Source AI in Python

This folder contains the materials for the tutorial (Hugging Face Transformers: Leverage Open-Source AI in Python)[https://realpython.com/huggingface-transformers-open-source-ai-in-python/].

Transformers is available on [PyPI](https://pypi.org/) and you can install it with [pip](https://realpython.com/what-is-pip/). Open a terminal or command prompt, create a new virtual environment, and then run the following command:

```console
(venv) $ python -m pip install transformers
```

This command will install the latest version of Transformers from PyPI onto your machine. Throughout this tutorial, you'll also leverage [PyTorch](https://realpython.com/pytorch-vs-tensorflow/) to interact with models at a lower level. You can install PyTorch with the following command:

```console
(venv) $ python -m pip install torch
```

To verify that the installations were successful, start a [Python REPL](https://realpython.com/python-repl/) and import `transformers` and `torch`:

```pycon
>>> import transformers
>>> import torch
```

If the imports run without errors, then you've successfully installed the dependencies needed for this tutorial.
