# Get Started With FastAPI

This repository contains code snippets discussed in the associated tutorial [Get Started With FastAPI](https://realpython.com/get-started-with-fastapi/).

## Installation

The recommended way to install FastAPI is with the [`[standard]`](https://github.com/fastapi/fastapi/blob/16d75d90eb96976a57b94cc24e4018859cd54c4d/pyproject.toml#L60) extra dependencies. This ensures you get all the tools you need for developing an API without having to hunt down additional packages later:

```console
$ python -m pip install "fastapi[standard]"
```

The quotes around `"fastapi[standard]"` ensure the command works correctly across different [terminals](https://realpython.com/terminal-commands/) and operating systems. With the command above, you install several useful packages, including the [FastAPI CLI](https://fastapi.tiangolo.com/fastapi-cli/) and [uvicorn](https://www.uvicorn.org/), an [ASGI](https://en.wikipedia.org/wiki/Asynchronous_Server_Gateway_Interface) server for running your application.

You can also use the `requirements.txt` file in this folder and run `python -m pip install -r requirements.txt` to install the standard dependencies of FastAPI.
