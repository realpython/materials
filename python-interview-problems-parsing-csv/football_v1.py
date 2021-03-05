#!/usr/bin/env python3
""" Find Minimum Goal Differential
    Write a program that takes a filename on the command line and processes the
    CSV contents. The contents will be a CSV file with end-of-season football
    standings for the English Premier League.
    Determine which team had the smallest goal differential that season.
    The first line of the CSV file will be column headers, with each subsequent
    line showing the data for one team:

        Team,Games,Wins,Losses,Draws,Goals For,Goals Against
        Arsenal,38,26,9,3,79,36

    The columns labeled "Goals" and "Goals Allowed" contain the total number of
    goals scored for and against each team in that season (so Arsenal scored 79
    goals against opponents and had 36 goals scored against them).

    Write a program to read the file, then print the name of the team with the
    smallest difference in "for" and "against" goals.  Create unit tests with
    Pytest to test your program.
"""
# import csv
