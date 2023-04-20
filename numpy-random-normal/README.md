# How to Get Normally Distributed Random Numbers With NumPy

This repository holds the code for the Real Python [How to Get Normally Distributed Random Numbers With NumPy](https://realpython.com/numpy-random-normal/) tutorial.

## Dependencies

The scripts use NumPy, Matplotlib, and SciPy. You should first create a virtual environment:

```console
$ python3 -m venv venv
$ source venv/bin/activate
```

You can then install the necessary packages with `pip`:

```console
(venv) $ python -m pip install numpy matplotlib scipy
```

Alternatively, you can install from [`requirements.txt`](requirements.txt) in order to get the same versions of dependencies that were used when developing and testing the code:

```console
(venv) $ python -m pip install -r requirements.txt
```

Use only one of the `pip install` commands.

## Run the Code

There are four scripts in this repository. The first three—[`normal_distribution.py`](normal_distribution.py), [`weights.py`](weights.py), and [`dice.py`](dice.py)—show code discussed in the tutorial. The final script, [`plot_normal_dist.py`](plot_normal_dist.py), contains the code used to generate the first figure in the tutorial.

Each script can be run with `python` inside your virtual environment:

```console
(venv) $ python normal_distribution.py
```

You can run the other scripts with a similar command.

## Author

- **Geir Arne Hjelle**, E-mail: [geirarne@realpython.com](geirarne@realpython.com)

## License

Distributed under the MIT license. See [`LICENSE`](../LICENSE) for more information.
