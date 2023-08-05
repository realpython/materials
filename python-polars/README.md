# Python Polars: A Lightning-Fast DataFrame Library

Supporting code for the article [Python Polars: A Lightning-Fast DataFrame Library](https://realpython.com/polars-python-lightening-fast-dataframe-library/). 

To run the code in this tutorial, you should have `polars`, `pandas`, `numpy`, `requests`, and `matplotlib` installed in your environment. 

If you want to install Polars with all of the library's optional dependencies, you can run:

```console
$ python -m pip install "polars[all]" requests matplotlib
```

Otherwise, you will at least need to include the `pandas` and `numpy` feature flags:

```console
$ python -m pip install "polars[numpy, pandas]" requests matplotlib
```