"""
This program gathers information from the temp_data.csv file about temperature
"""

import csv
from pkg_resources import resource_filename
from datetime import datetime
from datetime import timedelta
from typing import List, Dict
from collections import defaultdict


def get_temperature_data(filepath: str) -> Dict:
    """
    This function gets the temperature data from the csv file
    """
    with open(filepath) as csvfile:
        csv_reader = csv.DictReader(csvfile)
        data = {row["name"]: row for row in csv_reader}
        for value in data.values():
            value.pop("name")
        return data


def get_average_temp_by_date(
    date_string: str, temperature_data: Dict
) -> float:
    """
    This function gets the average temperature for all the samples
    taken by the students by date

    :param date_string:             date to find average temperature for
    :param connection:              database connection
    :return:                        average temp for date, or None if not found
    """
    # Target date
    target_date = datetime.strptime(date_string, "%Y-%m-%d").date()

    # Iterate through the data and get the data
    data = []
    for samples in temperature_data.values():

        # Iterate through the samples
        for sample_date, sample in samples.items():

            # Generate a date range for the sample
            min_date = datetime.strptime(
                sample_date, "%Y-%m-%d"
            ).date() + timedelta(days=-3)
            max_date = datetime.strptime(
                sample_date, "%Y-%m-%d"
            ).date() + timedelta(days=3)
            if min_date <= target_date <= max_date:
                data.append(float(sample))

    # Get the average temp
    return sum(data) / len(data)


def get_average_temp_sorted(direction: str, temperature_data: Dict) -> List:
    dir = direction.lower()
    if dir not in ["asc", "desc"]:
        raise Exception(f"Unknown direction: {direction}")

    results = defaultdict(int)
    for data in temperature_data.values():
        for date, value in data.items():
            results[date] += float(value)

    for date, total in results.items():
        results[date] = float(total) / float(len(temperature_data.keys()))

    # Convert dictionary to list
    results = results.items()

    # Sort the list in the appropriate order
    return sorted(
        results, key=lambda v: v[1], reverse=False if dir == "asc" else True
    )


def main():
    print("starting")

    # Get the temperature data into a dictionary structure
    filepath = resource_filename("project.data", "temp_data.csv")
    temperature_data = get_temperature_data(filepath)

    # Get the average temperature by date
    date_string = "2019-02-10"
    average_temp = get_average_temp_by_date(date_string, temperature_data)
    print(f"Average temp {date_string}: {average_temp:.2f}")
    print()

    # Get the average temps for the year sorted ascending or descending
    average_temps = get_average_temp_sorted("asc", temperature_data)
    for date, average_temp in average_temps:
        print(f"Date: {date}, average temp: {average_temp:.2f}")
    print()

    print("finished")


if __name__ == "__main__":
    main()
