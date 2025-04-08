# Modern Web Automation With Python and Selenium

This repository contains the module `bandcamp`, which is the sample app built in the Real Python tutorial [Modern Web Automation With Python and Selenium](https://realpython.com/modern-web-automation-with-python-and-selenium/).

## Installation and Setup

Create and activate a [Python virtual environment](https://realpython.com/python-virtual-environments-a-primer/).

Then, install the requirements:

```sh
(venv) $ python -m pip install -r requirements.txt
```

The only direct dependency for this project is [Selenium](https://selenium-python.readthedocs.io/). You should use a Python version of at least 3.10, which is necessary to support [structural pattern matching](https://realpython.com/structural-pattern-matching/).

You'll need a [Firefox Selenium driver](https://selenium-python.readthedocs.io/installation.html#drivers) called `geckodriver` to run the project as-is. Make sure to [download and install](https://github.com/mozilla/geckodriver/releases) it before running the project.

## Run the Bandcamp Discover Player

To run the music player, install the package, then use the entry point command from your command-line:

```sh
(venv) $ python -m pip install .
(venv) $ bandcamp-player
```

You'll see a text-based user interface that allows you to interact with the music player:

```
Type: play [<track_number>] | pause | tracks | more | exit
>
```

Type one of the available commands to interact with Bandcamp's Discover section through your headless browser. Listen to songs with `play`, pause the current song with `pause` and restart it with `play`. List available tracks with `tracks`, and load more songs using `more`. You can exit the music player by typing `exit`.

## Troubleshooting

If the music player seems to hang when you run the script, confirm whether you've correctly set up your WebDriver based on the following points.

### Version Compatibility

Confirm that your browser and corresponding WebDriver are in sync. If you followed the previous suggestion, then you should be using Firefox and geckodriver. If that doesn't work for any reason, you may need to switch browser _and_ WebDriver.

For example, if you're using Chrome, then you need to install ChromeDriver and it must match your Chrome version. Otherwise, you may run into errors like `SessionNotCreatedException`.
For more details, refer to the official [ChromeDriver documentation](https://sites.google.com/chromium.org/driver/) or [geckodriver releases](https://github.com/mozilla/geckodriver/releases).

### Driver Installation and Path Issues

Once you've confirmed that your browser and driver match, make sure that the WebDriver executable is properly installed:

- **Path Configuration:** The driver must be in your system's PATH, or you need to specify its full path in your code.
- **Permissions:** Ensure the driver file has the necessary execution permissions.

If you're still running into issues executing the script, then consult the [Selenium Documentation](https://www.selenium.dev/documentation/) for additional troubleshooting tips or leave a comment on the tutorial.

## About the Authors

Martin Breuss - Email: martin@realpython.com
Bartosz Zaczyński - Email: bartosz@realpython.com

## License

Distributed under the MIT license.
