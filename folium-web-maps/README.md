# Python Folium: Create Web Maps From Your Data

This directory contains code associated with the Real Python tutorial [Python Folium: Create Web Maps From Your Data](https://realpython.com/python-folium-web-maps-from-data/). For additional information, please visit the tutorial link.

## Installation

Create and activate a virtual environment, then install `folium` and `pandas`. For the specific versions used in the tutorial, you can install from `requirements.txt`:

```sh
$ python -m venv venv
$ source venv/bin/activate
# PS> venv\Scripts\activate
(venv) $ python -m pip install -r requirements.txt
```

If you also want to work with the included [Jupyter notebook file](footprint.ipynb), then you need to additionally install `jupyter`:

```sh
(venv) $ python -m pip install jupyter
```

## Usage

You can re-create [the HTML file](footprint.html) by running [`footprint.py`](footprint.py) from within your virtual environment.

You can modify the code to make it work with your own dataset.

Additionally, you can take a look at how Jupyter renders Folium maps directly inside of a notebook by checking out [`footprint.ipynb`](footprint.ipynb).

## About the Author

Martin Breuss - Email: martin@realpython.com

## License

Distributed under the MIT license. See `LICENSE` in the root directory of this `materials` repo for more information.
