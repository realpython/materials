# Working With Linear Systems in Python

This directory contains code associated with the Real Python tutorials:

- [Working With Linear Systems in Python With `scipy.linalg`](https://realpython.com/python-scipy-linalg/)
- [Linear Algebra in Python: Matrix Inverses and Least Squares](https://realpython.com/python-linear-algebra/)

See the tutorials for details.

## Installation

Use [`conda`](https://docs.conda.io/en/latest/miniconda.html) to create and activate a virtual environment:

```console
$ conda create --name linalg
$ conda activate linalg
```

Install packages into your environment:

```console
(linalg) $ conda install numpy scipy matplotlib pandas jupyter
```

## Code

The code from the tutorials is available as notebooks that you can open with [Jupyter](https://realpython.com/jupyter-notebook-introduction/):

- Working With Linear Systems in Python With `scipy.linalg` [notebook](linear-systems.ipynb)
- Linear Algebra in Python: Matrix Inverses and Least Squares [notebook](matrix-inverses-least-squares.ipynb)

## Data

You can find [`vehicles_cleaned.csv`](vehicles_cleaned.csv) in this directory. The dataset is adapted from https://www.kaggle.com/austinreese/craigslist-carstrucks-data and used in Linear Algebra in Python: Matrix Inverses and Least Squares. The [vehicles-data-preparation](vehicles-data-preparation.ipynb) notebook shows how the dataset was cleaned and prepared.

## About the Author

Renato Candido - <https://realpython.com/team/rcandido/> 

## License

Distributed under the MIT license. See [`LICENSE`](../LICENSE) for more information.
