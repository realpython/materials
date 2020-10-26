# Use Sentiment Analysis With Python to Classify Reviews

Resources and materials for Real Python's [Use Sentiment Analysis With Python to Classify Reviews](https://realpython.com/use-sentiment-analysis-python-classify-movie-reviews/) tutorial.

## Installation

Create and activate a new virtual environment:

```shell
$ python -m venv .venv
$ source .venv/bin/activate
```

Install Python dependencies into the active virtual environment:

```shell
(.venv) $ python -m pip install -r requirements.txt
```

Download English model for spaCy:

```shell
(.venv) $ python -m spacy download en_core_web_sm
```

Download and extract the [Large Movie Review Dataset](https://ai.stanford.edu/~amaas/data/sentiment/) compiled by [Andrew Maas](http://www.andrew-maas.net/):

```shell
$ curl -s https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz | tar xvz
```

## Usage

Get the sentiment of a movie review stored in the `TEST_REVIEW` variable:

```shell
(.venv) $ python sentiment_analyzer.py
```
