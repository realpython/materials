#!/usr/bin/env python

"""
Fetch and parse people names from the IMDb.

Usage:
$ python download_imdb.py
"""

import gzip
import shutil
import tempfile
import urllib.request


def main():
    """Script entry point."""

    print('Fetching data from IMDb...')

    with open('names.txt', 'w') as destination:
        destination.writelines(names())

    with open('names.txt') as source, \
         open('sorted_names.txt', 'w') as destination:
        destination.writelines(sorted(source.readlines()))

    print('Created "names.txt" and "sorted_names.txt"')


def names():
    """Return a generator of names with a trailing newline."""
    url = 'https://datasets.imdbws.com/name.basics.tsv.gz'
    with urllib.request.urlopen(url) as response:
        with tempfile.NamedTemporaryFile(mode='w+b') as archive:
            shutil.copyfileobj(response, archive)
            archive.seek(0)
            with gzip.open(archive, mode='rt') as source:
                next(source)  # Skip the header
                for line in source:
                    full_name = line.split('\t')[1]
                    yield f'{full_name}\n'


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Aborted')
