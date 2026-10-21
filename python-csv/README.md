# Reading and Writing CSV Files in Python

This folder provides the code examples for the Real Python tutorial [Reading and Writing CSV Files in Python](https://realpython.com/python-csv/).

Consider creating a [Python virtual environment](https://realpython.com/python-virtual-environments-a-primer/) before installing the dependencies:

```shell
$ python3 -m venv .venv/ --prompt python-csv
$ source .venv/bin/activate
(python-csv) $ python -m pip install -r requirements.txt
```

The scripts read their data files from the current working directory, so run them from inside this folder:

```shell
(python-csv) $ python read_csv_with_reader.py
```

Each script holds the code from one section of the tutorial:

| File | Tutorial section |
| --- | --- |
| `read_csv_with_reader.py` | Reading CSV Files With `csv` |
| `read_csv_into_dictionary.py` | Reading CSV Files Into a Dictionary With `csv` |
| `write_csv_with_writer.py` | Writing CSV Files With `csv` |
| `write_csv_from_dictionary.py` | Writing CSV File From a Dictionary With `csv` |
| `read_csv_with_pandas.py` | Reading CSV Files With `pandas` |
| `write_csv_with_pandas.py` | Writing CSV Files With `pandas` |

The examples that the tutorial shows at the interactive prompt are included in
`read_csv_with_pandas.py` as `print()` calls, in the same order as the article,
so that you can run the whole section as a single script.

There are also three data files used throughout the tutorial:

| File | Description |
| --- | --- |
| `employee_birthday.csv` | Employee names, departments, and birthday months read by the `csv` examples. |
| `employee_addresses.csv` | Addresses containing an embedded comma, used to illustrate the optional `reader` parameters. |
| `hrdata.csv` | Employee hire dates, salaries, and sick days read by the `pandas` examples. |

Running the writing examples creates `employee_file.csv`, `employee_file2.csv`,
and `hrdata_modified.csv` in this folder. Those files aren't checked in, since
the tutorial generates them.
