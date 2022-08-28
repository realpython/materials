# When Do You Use an Ellipsis in Python?

This repository holds the code for the Real Python [When Do You Use an Ellipsis in Python?](https://realpython.com/python-ellipsis/) tutorial.

## Dependencies

To run the examples of this repository, you need to have the dependencies installed. You should first create a virtual environment:

```console
$ python -m venv venv
$ source venv/bin/activate
```

Then, navigate into the subfolder and install the requirementes with `pip`:

```console
(venv) $ python -m pip install -r requirements.txt
```

The requirements are separated for each example, so you can decide which you want to install into your virtual environment.

## Run the Flask Stub Example

Enter the `flask_stub_example/` folder. You can then run the Flask server in debug mode with this command:

```console
(venv) $ flask --app app --debug run
...
```

You can visit `http://127.0.0.1:5000/` in your browser to see the "Hello, world!" message.

## Run the Type Hints Example

Enter the `type_hints_examples/` folder and run the files with `mypy`:

```console
(venv) $ mypy tuple_example.py
...
(venv) $ mypy callable_example.py
...
```

## Run the NumPy Example

Enter the `numpy_example/` folder and run this command:

```console
(venv) $ python numpy_no_ellipsis_example.py
```

## Author

- **Philipp Acsany**, E-mail: [philipp@realpython.com](philipp@realpython.com)

## License

Distributed under the MIT license. See [`LICENSE`](../LICENSE) for more information.
