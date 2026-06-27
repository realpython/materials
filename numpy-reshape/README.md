# Using NumPy reshape() to Change the Shape of an Array

This folder contains the sample code and image that accompany the Real Python
tutorial [Using NumPy reshape() to Change the Shape of an Array](https://realpython.com/numpy-reshape/).

## Setup

Create and activate a virtual environment, then install the requirements:

```console
$ python -m venv venv
$ source venv/bin/activate
(venv) $ python -m pip install -r requirements.txt
```

## Scripts

Each script is self-contained and mirrors one section of the tutorial. The
scripts that use random data seed the generator so that the output is
reproducible.

| Script | Tutorial section |
| --- | --- |
| `array_shape.py` | Understand the shape of NumPy arrays |
| `change_shape.py` | Change an array's shape using `reshape()` |
| `reduce_dimensions.py` | Reduce an array's number of dimensions |
| `increase_dimensions.py` | Increase an array's number of dimensions |
| `compatible_shapes.py` | Ensure the new shape is compatible |
| `order_parameter.py` | Control how data is rearranged using `order` |
| `color_image.py` | Reduce a 3D color image to two dimensions |
| `wildcard.py` | Use `-1` as an argument in `reshape()` |

Run any script with Python:

```console
(venv) $ python change_shape.py
```

`color_image.py` reads `poppy.jpg` from this folder and opens the reshaped
images in your default image viewer, so run it from this directory.

## Image Credit

- poppy.jpg: [Pixabay](https://pixabay.com/photos/poppy-summer-red-nature-flower-2381645/) by [kellepics](https://pixabay.com/users/kellepics-4893063/)
