#!/usr/bin/env python3
""" Find Minimum Goal Differential
    Write a program that takes a filename on the command line and processes the
    CSV contents. The contents will be a CSV file with end-of-season football
    standings for the English Premier League.
    Determine which team had the smallest goal differential that season.
    The first line of the CSV file will be column headers:

        Team,Games,Wins,Losses,Draws,Goals For,Goals Against

    Write unit tests with Pytest to test your program.
"""
import csv


def get_next_name_and_diff(csv_file):
    for team_stats in csv.DictReader(csv_file):
        diff = int(team_stats["Goals For"]) - int(team_stats["Goals Against"])
        yield team_stats["Team"], abs(diff)


def get_min_score_difference(filename):
    with open(filename, "r", newline="") as csv_data:
        return min(get_next_name_and_diff(csv_data), key=lambda item: item[1])
