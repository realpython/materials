#!/usr/bin/env python3
""" Reusable CSV parser for both football and weather data.  """
import csv


def get_next_result(csv_file, func):
    for stats in csv.DictReader(csv_file):
        yield func(stats)
