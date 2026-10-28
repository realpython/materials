# How to Use Generators and yield in Python

This folder provides the code examples for the Real Python tutorial [How to Use Generators and yield in Python](https://realpython.com/introduction-to-python-generators/).

The scripts only use Python's standard library. They read `techcrunch.csv` from the current working directory, so run them from inside this folder:

```shell
$ python data_pipeline.py
Total series A fundraising: $4380015000
```

Each script holds the code from one section of the tutorial:

| File | Tutorial section |
| --- | --- |
| `csv_reader.py` | Example 1: Reading Large Files |
| `infinite_sequence.py` | Example 2: Generating an Infinite Sequence |
| `palindromes.py` | Example 3: Detecting Palindromes |
| `advanced_gen.py` | Using Advanced Generator Methods |
| `data_pipeline.py` | Creating Data Pipelines With Generators |
| `techcrunch.csv` | The data set for Example 1 and the data pipeline |

`infinite_sequence.py` and `palindromes.py` run forever, so press <kbd>Ctrl</kbd>+<kbd>C</kbd> to stop them. `advanced_gen.py` takes the generator method to demonstrate as an argument:

```shell
$ python advanced_gen.py send   # Runs until you press Ctrl+C
$ python advanced_gen.py throw  # Stops with a ValueError
$ python advanced_gen.py close  # Stops with StopIteration
```
