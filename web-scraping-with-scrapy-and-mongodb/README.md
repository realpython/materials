# Web Scraping With Scrapy and MongoDB

[Web Scraping With Scrapy and MongoDB](https://realpython.com/web-scraping-with-scrapy-and-mongodb/) is an example project for building a robust web scraper for static sites leveraging Scrapy and MongoDB.

## Installation and Setup

1. Create a Python virtual environment

```sh
$ python -m venv ./venv
$ source venv/bin/activate
(venv) $
```

2. Install the requirements

```sh
(venv) $ pip install -r requirements.txt
```

You'll also need to [set up a MongoDB collection](https://realpython.com/web-scraping-with-scrapy-and-mongodb/#set-up-a-mongodb-collection-on-your-computer) like described in the tutorial.

## Run the Scraper

Navigate into the `books/` project directory.

Then you can start crawling the site:

```sh
(venv) $ scrapy crawl book
```

If set up correctly, this will populate your MongoDB collection with the book information scraped from the example site.

## About the Author

Martin Breuss - Email: martin@realpython.com

## License

Distributed under the MIT license. See ``LICENSE`` for more information.
