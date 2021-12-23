# Implementing a Hash Table in Python

Code supplementing the tutorial [Implementing a Hash Table in Python](https://realpython.com/python-hash-table/).

## Installation

To get started, create and activate a new virtual environment, and then install the required dependencies into it:

```shell
$ python3 -m venv venv --prompt=hashtable
$ source venv/bin/activate
(hashtable) $ python -m pip install -r requirements.txt
```

## Usage

Run the unit tests, remembering to seed the Python's hash randomizer with a value that won't cause false positives:

```shell
(hashtable) $ export PYTHONHASHSEED=128
(hashtable) $ pytest 01_hashtable_prototype/
(hashtable) $ pytest 02_linear_probing/
(hashtable) $ pytest 03_autoresize/
(hashtable) $ pytest 04_load_factor/
(hashtable) $ pytest 05_separate_chaining/
(hashtable) $ pytest 06_insertion_order/
```
