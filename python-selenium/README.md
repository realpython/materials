# Modern Web Automation With Python and Selenium

This repository contains the module `bandcamp`, which is the sample app built in the Real Python tutorial [Modern Web Automation With Python and Selenium](https://realpython.com/modern-web-automation-with-python-and-selenium/).

## Installation and Setup

Create and activate a [Python virtual environment](https://realpython.com/python-virtual-environments-a-primer/).

Then, install the requirements:

```sh
(venv) $ python -m pip install -r requirements.txt
```

The only direct dependency for this project is [Selenium](https://selenium-python.readthedocs.io/). You should use a Python version of at least 3.8.

## Run the Bandcamp Discover Player

To run the music placer, navigate to the `src/` folder, then execute the module from your command-line:

```sh
(venv) $ cd src/
(venv) $ python -m bandcamp
```

You'll see a text-based user interface that allows you to interact with the music player:

```
Type: [play <track number>], [tracks], [more], [exit]
>
```

Type one of the available commands to interact with Bandcamp's Discover section through your headless browser. Listen to songs with `play`, list available tracks with `tracks`, and load more songs using `more`. You can exit the music player by typing `exit`.

## About the Authors

Martin Breuss - Email: martin@realpython.com
Bartosz Zaczyński - Email: bartosz@realpython.com

## License

Distributed under the MIT license. See ``LICENSE`` for more information.
