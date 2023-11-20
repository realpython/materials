# The Python Rich Package: Unleash the Power of Console Text

This repository holds the sample code for the Real Python [showcase](https://realpython.com/python-rich-package).

## Dependencies

You should start by creating a virtual environment:

```console
$ python -m venv venv
$ source venv/bin/activate
```

Next, install `rich` with `pip`:

```console
(venv) $ python -m pip install rich
```

The tutorial includes static sample data for the scrolling cryptocurrency table. This is also included in this repository as `crypto_data.json`. 
If you want to download your own fresh data, then you'll need the `requests` package:

```console
(venv) $ python -m pip install requests
```

The code to perform the download is in `get_crypto_data.py`. This demo code demonstrates a single request, which it then dumps to the screen. For a real-time application, you'd need to execute this request and process the data in a loop. The [CoinLore website](https://www.coinlore.com/cryptocurrency-data-api) doesn't impose rate limits, but they suggest making at most one request per second.

## Author

[Charles de Villiers](https://realpython.com/team/cdevilliers/)

## License

Distributed under the MIT license. See `LICENSE` in the root directory of this `materials` repo for more information.
