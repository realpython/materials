# Pygame: A Primer on Game Programming in Python

The code in this folder supplements the Real Python tutorial [Pygame: A Primer on Game Programming in Python](https://realpython.com/pygame-a-primer/).

## Dependencies

The tutorial uses Python 3.13 and pygame 2.6.1. First create and activate a virtual environment:

```console
$ python -m venv venv
$ source venv/bin/activate
```

Then install `pygame` with `pip`:

```console
(venv) $ python -m pip install pygame
```

Alternatively, you can install the pinned version used in the tutorial from `requirements.txt`:

```console
(venv) $ python -m pip install -r requirements.txt
```

## Run the Examples

Run each script from inside this folder so that the images and sounds resolve:

```console
(venv) $ python pygame_simple.py
(venv) $ python py_tutfinal.py
(venv) $ python py_tut_with_images.py
```

- `pygame_simple.py` is the basic `pygame` program from the beginning of the tutorial.
- `py_tutfinal.py` is the game built with plain `Surface` objects.
- `py_tut_with_images.py` is the final game with sprite images, clouds, and sound.

Use the arrow keys to move the jet, and press <kbd>Esc</kbd> or close the window to quit.
