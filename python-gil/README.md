# What Is the Python Global Interpreter Lock (GIL)?

This folder provides the code examples for the Real Python tutorial [What Is the Python Global Interpreter Lock (GIL)?](https://realpython.com/python-gil/).

The tutorial shows some of its examples at the REPL. Those are provided here as
runnable scripts that print the values the tutorial discusses:

| Script | Tutorial section |
| --- | --- |
| `reference_counting.py` | What Problem Did the GIL Solve for Python? |
| `single_threaded.py` | The Impact on Multi-Threaded Python Programs |
| `multi_threaded.py` | The Impact on Multi-Threaded Python Programs |
| `switch_interval.py` | Why Wasn't It Removed in Python 3? |
| `multiprocess.py` | How to Deal With Python's GIL |

## Running the Examples

The examples only use the Python standard library, so there's nothing to
install. Create and activate a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/),
then run any of the scripts:

```sh
$ python -m venv venv/
$ source venv/bin/activate
(venv) $ python single_threaded.py
```

The timings printed by `single_threaded.py`, `multi_threaded.py`, and
`multiprocess.py` depend on your machine, so they won't match the numbers in
the tutorial exactly. What matters is how they compare to each other.
