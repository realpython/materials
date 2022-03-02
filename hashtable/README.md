# Build a Hash Table in Python With TDD

Code supplementing the [tutorial on the hash table](https://realpython.com/python-hash-table/) hosted on Real Python.

## Installation

To get started, create and activate a new virtual environment, and then install the required dependencies into it:

```shell
$ python3 -m venv venv --prompt=hashtable
$ source venv/bin/activate
(hashtable) $ python -m pip install -r requirements.txt
```

## Usage

Use the subfolders in the parent folder `01_hashtable_prototype/` as control checkpoints or when you're lost while going through the tutorial. Remember that these tests require you to seed Python's hash randomizer with a value that won't cause false positives, for example:

```shell
(hashtable) $ PYTHONHASHSEED=128 pytest 01_hashtable_prototype/01_define_a_custom_hashtable_class
```

The remaining parent folders contain test cases that don't need that environment variable to be set anymore: 

```shell
(hashtable) $ pytest 02_linear_probing/
(hashtable) $ pytest 03_autoresize/
(hashtable) $ pytest 04_load_factor/
(hashtable) $ pytest 05_separate_chaining/
(hashtable) $ pytest 06_insertion_order/
```
