# The Python Rich Package: Unleash the Power of Console Text

This repository holds the sample code for the Real Python [showcase](https://realpython.com/exploring-python-rich-package).

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
The article includes sytatic sample data for the scrolling cryptocurrency table - this is also included in this repository as rich_showcase_data.py. 
If you want to download your own data in real time, you will need the `requests` package:

```console
(venv) $ python -m pip install requests
```
The code to perform the download is in get_rich_showcase_data.py. This demo code demonstrates a single request, which it then dumps to the screen; for a real-time application you would need to execute this request and process the data in a loop. The [CoinLore website](https://www.coinlore.com/cryptocurrency-data-api) doesn't impose rate limits, but they suggest making one request per second.

There is a Jupyter notebook containing all the sample code from the article.

## Author

Charles de Villiers

## License
Distributed under the MIT license. See `LICENSE` in the root directory of this `materials` repo for more information.
