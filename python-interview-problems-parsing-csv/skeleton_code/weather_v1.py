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
# import csv
