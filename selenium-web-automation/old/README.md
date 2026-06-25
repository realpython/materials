# Modern Web Automation With Python and Selenium

This folder contains the code for the Real Python tutorial on [Modern Web Automation With Python and Selenium](https://realpython.com/modern-web-automation-with-python-and-selenium/).

## Setup

Create and activate a virtual environment, then install the dependencies:

```sh
(venv) $ python -m pip install -r requirements.txt
```

## Usage

To start streaming music from BandCamp's _Discover_ section, you can execute the script:

```sh
(venv) $ python player.py
```

This will instantiate a `BandLeader` object and call it's `.stream()` method. Music should start playing and you'll see information about the tracks you'll listen to printed to your console.

If you want to interact with the class in a different way, then you can start a REPL session and import `BandLeader`, then go from there:

```python
>>> from player import BandLeader
>>> b = BandLeader()
>>> dir(b)
```

The class will record a history of the songs you listen to in a CSV file.

## Author

Martin Breuss – martin@realpython.com

## License

This project is distributed under the MIT license.
