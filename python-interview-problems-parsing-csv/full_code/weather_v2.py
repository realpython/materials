#!/usr/bin/env python3
""" Find the day with the highest average temperature.
    Write a program that takes a filename on the command line and processes the
    CSV contents. The contents will be a CSV file with a month of weather data,
    one day per line.

    Determine which day had the highest average temperature where the average
    temperature is the average of the day's high and low temperatures. This is
    not normally how average temperature is computed, but it will work for our
    demonstration.

    The first line of the CSV file will be column headers:

        Day,MxT,MnT,AvT,AvDP,1HrP TPcn,PDir,AvSp,Dir,MxS,SkyC,MxR,Mn,R AvSLP

    The day number, max temperature, and min temperature are the first three
    columns.

    Write unit tests with Pytest to test your program.
"""
import csv


def get_day_and_avg(day_stats):
    day_number = int(day_stats["Day"])
    avg = (int(day_stats["MxT"]) + int(day_stats["MnT"])) / 2
    return day_number, avg


def get_next_day_and_avg(csv_file, func):
    for day_stats in csv.DictReader(csv_file):
        yield func(day_stats)


def get_max_avg(filename):
    with open(filename, "r", newline="") as csv_file:
        return max(
            get_next_day_and_avg(csv_file, get_day_and_avg),
            key=lambda item: item[1],
        )
