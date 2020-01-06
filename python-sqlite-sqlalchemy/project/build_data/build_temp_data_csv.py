import csv
import datetime
from random import randint
from pkg_resources import resource_filename


start_date = datetime.datetime.strptime("2019-01-02", "%Y-%m-%d")

students = [
    "John",
    "Mary",
    "Susan",
    "Doug",
    "Andrew",
    "George",
    "Martha",
    "Paul",
    "Helen",
]

temperature_data = [
    10,
    12,
    16,
    23,
    13,
    12,
    14,
    22,
    25,
    28,
    32,
    33,
    37,
    36,
    35,
    40,
    44,
    45,
    50,
    52,
    58,
    60,
    66,
    70,
    70,
    72,
    78,
    80,
    81,
    82,
    85,
    88,
    90,
    87,
    90,
    85,
    82,
    81,
    78,
    75,
    72,
    72,
    70,
    63,
    65,
    62,
    60,
    45,
    40,
    37,
    30,
    28,
]


def offset_temp(temperature):
    """
    This function modifies the temperature +/- a random
    amount up to 10
    :param temperature:     temperature to modify
    :return:                modified temperature
    """
    return temperature + randint(-10, 10)


def main():
    # create the CSV file
    csv_filepath = resource_filename("project.data", "temp_data.csv")

    with open(csv_filepath, "w") as data_fh:

        # create the writer
        csv_writer = csv.writer(data_fh)

        # write the header
        header = ["name"]
        for week in range(0, 52):
            current_date = start_date + datetime.timedelta(days=week * 7)
            header.append(current_date.strftime("%Y-%m-%d"))
        csv_writer.writerow(header)

        # iterate through the students and write their data
        for student in students:
            data = [student]
            # iterate through the weeks
            for week in range(0, 52):
                data.append(offset_temp(temperature_data[week]))

            csv_writer.writerow(data)


if __name__ == "__main__":
    main()
