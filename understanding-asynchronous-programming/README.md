# Async Programming in Python: From Generators to `asyncio`

This folder provides the code examples for the Real Python tutorial [Async Programming in Python: From Generators to `asyncio`](https://realpython.com/python-async-features/).

To run the examples, first create and activate a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/). Then, install the required libraries into it:

```sh
$ python -m venv venv/
$ source venv/bin/activate
(venv) $ python -m pip install -r requirements.txt
```

The examples require Python 3.11 or later, because they use `asyncio.TaskGroup` and `asyncio.timeout()`. The `python -m asyncio pstree` command shown in the tutorial requires Python 3.14 or later.
