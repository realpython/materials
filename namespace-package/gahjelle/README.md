In a "thin" convention, I've named the projects (the outer folders) with a dash, and the source directories (the inner folders) with underscore.

# Installation

Create a virtual environment and install dependencies from `requirements.txt`.

Then install `data-repo` and `snake-data` using their empty `pyproject.toml` files:

```console
$ python -m pip install -e data-repo/
$ python -m pip install -e snake-data/
```

# Usage

Run the following session from anywhere except inside the `snake-corp/` directory:

```pycon
>>> from data_repo import read

>>> read.data("cars")
     Make  Year
0   Honda  2017
1  Toyota  2022

>>> read.path("cars")
PosixPath('/home/namespacer/data-repo/data_repo/articles/cars.csv')

>>> read.data("trains")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/namespacer/data-repo/data_repo/read.py", line 18, in data
    raise FileNotFoundError(f"{name} not found in {package}")
FileNotFoundError: trains not found in data_repo
```

Note that `trains` (from `snake_corp` is not available).

The `snake-data` project shows a way to reuse the `data-repo` package locally, without including the same datasets:

```pycon
>>> from snake_data import read as local_read

>>> local_read.data("cars")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/namespacer/data-repo/data_repo/read.py", line 18, in data
    raise FileNotFoundError(f"{name} not found in {package}")
FileNotFoundError: cars not found in snake_data

>>> local_read.data("programmering")
  Language   BDFL
0   Python  Guido
1   Elixir   Josè
2     Java  James

>>> local_read.path("programmering")
PosixPath('/home/namespacer/snake-data/snake_data/programmering.csv')
```

Now, exit the REPL and move to the `snake-corp/` folder before running the REPL one more time:

```pycon
>>> from data_repo import read

>>> read.data("cars")
     Make  Year
0   Honda  2017
1  Toyota  2022

>>> read.data("trains")
   Brand Country
0     Vy  Norway
1  Renfe   Spain
2    FGC   Spain

>>> read.path("trains")
PosixPath('/home/namespacer/snake-corp/data_repo/trains.csv')
```

Now, all the regular data files, as well as the SnakeCorp data files are available.
