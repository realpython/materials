# Pythonic Data Cleaning With pandas and NumPy

The materials contained in this download are designed to complement the Real Python tutorial [Pythonic Data Cleaning With pandas and NumPy](https://realpython.com/python-data-cleaning-numpy-pandas/).

Consider creating a [Python virtual environment](https://realpython.com/python-virtual-environments-a-primer/) before installing the dependencies:

```shell
$ python -m venv venv/ --prompt data-cleaning
$ source venv/bin/activate
(data-cleaning) $ python -m pip install -r requirements.txt jupyterlab
```

Your download bundle contains:

- `data_cleaning.ipynb`, a Jupyter notebook with the code from the tutorial, in the same order
- `Datasets/BL-Flickr-Images-Book.csv`, information about books from the British Library
- `Datasets/university_towns.txt`, the names of college towns in every US state
- `Datasets/olympics.csv`, a summary of every country's participation in the Summer and Winter Olympics

Start JupyterLab from this folder with `jupyter lab` and open the notebook, so that the `Datasets/` paths resolve.

The code was tested with Python 3.15, pandas 3.1.0, and NumPy 2.5.4.
