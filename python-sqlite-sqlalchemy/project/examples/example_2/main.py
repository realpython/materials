"""
This program gathers information from the database file about temperature
"""

from pkg_resources import resource_filename
from datetime import datetime
from datetime import timedelta
import sqlite3


def get_average_temp_by_date(date_string, connection):
    """
    This function gets the average temperature for all the samples
    taken by the students by date

    :param date_string:             date to find average temperature for
    :param connection:              database connection
    :return:                        average temp for date, or None if not found
    """
    # Target date
    target_date = datetime.strptime(date_string, "%Y-%m-%d").date()
    min_date = target_date + timedelta(days=-3)
    max_date = target_date + timedelta(days=3)

    cursor = connection.cursor()
    sql = """
        SELECT
          avg(value) as average
        FROM temperature_data
        WHERE date between ? and ?
    """
    result = cursor.execute(sql, (min_date, max_date)).fetchone()
    return result[0] if result else None


def get_average_temp_sorted(direction: str, connection) -> list:

    dir = direction.lower()
    if dir not in ["asc", "desc"]:
        raise Exception(f"Unknown direction: {direction}")

    cursor = connection.cursor()
    sql = f"""
        SELECT
            date,
            AVG(value) as average_temp
        FROM temperature_data
        GROUP BY date
        ORDER BY average_temp {dir}
    """
    results = cursor.execute(sql).fetchall()
    return results


def main():
    print("starting")

    # Connect to the sqlite database
    sqlite_filepath = resource_filename("project.data", "temp_data.db")
    connection = sqlite3.connect(sqlite_filepath)

    # Get the average temperature by date
    date_string = "2019-02-10"
    average_temp = get_average_temp_by_date(date_string, connection)
    print(f"Average temp {date_string}: {average_temp:.2f}")
    print()

    # Get the average temps for the year sorted ascending or descending
    average_temps = get_average_temp_sorted("asc", connection)
    for date, average_temp in average_temps:
        print(f"Date: {date}, average temp: {average_temp:.2f}")
    print()

    print("finished")


if __name__ == "__main__":
    main()
