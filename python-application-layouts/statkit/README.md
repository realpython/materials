# statkit

A small statistics helper library in a `src/` layout. It provides `mean()`,
`median()`, `stdev()`, `pearson()`, and `spearman()` using only the standard
library.

## Installation

Because of the `src/` layout, you need to install the package before you can
import it:

```console
$ python -m pip install -e ".[dev]"
```

## Usage

```pycon
>>> from statkit import mean, median, pearson, spearman
>>> mean([1, 2, 3, 4])
2.5
>>> median([4, 1, 3, 2])
2.5
>>> pearson([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
0.9811049102515929
>>> spearman([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
1.0
```

## Running the Tests

```console
$ python -m pytest
```
