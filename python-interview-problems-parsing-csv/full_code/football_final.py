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
import csv_reader


def get_name_and_diff(team_stats):
    diff = int(team_stats["Goals For"]) - int(team_stats["Goals Against"])
    return team_stats["Team"], abs(diff)


def get_min_score_difference(filename):
    with open(filename, "r", newline="") as csv_data:
        return min(
            csv_reader.get_next_result(csv_data, get_name_and_diff),
            key=lambda item: item[1],
        )
