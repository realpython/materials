"""
This program gathers information from the temp_data.csv file about temperature
"""

from pkg_resources import resource_filename
from datetime import datetime
from datetime import timedelta
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Float, Date
from sqlalchemy.sql import func, and_, asc, desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TemperatureData(Base):
    __tablename__ = "temperature_data"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(Date)
    value = Column(Float)


def get_average_temp_by_date(date_string, session) -> float:
    """
    This function gets the average temperature for all the samples
    taken by the students by date

    :param date_string:             date to find average temperature for
    :param session:                 SqlAlchemy session
    :return:                        average temp for date, or None if not found
    """
    target_date = datetime.strptime(date_string, "%Y-%m-%d").date()
    min_date = target_date + timedelta(days=-3)
    max_date = target_date + timedelta(days=3)

    result = (
        session.query(func.avg(TemperatureData.value))
        .filter(
            and_(
                TemperatureData.date >= min_date,
                TemperatureData.date <= max_date,
            )
        )
        .one()
    )
    return result[0]


def get_average_temp_sorted(direction: str, session) -> list:
    if direction.lower() not in ["asc", "desc"]:
        raise Exception(f"Unknown direction: {direction}")

    dir = asc if direction.lower() == "asc" else desc

    results = (
        session.query(
            TemperatureData.date,
            func.avg(TemperatureData.value).label("average_temp"),
        )
        .group_by(TemperatureData.date)
        .order_by(dir("average_temp"))
        .all()
    )
    return results


def main():
    print("starting")

    # Connect to the database using SqlAlchemy
    sqlite_filepath = resource_filename("project.data", "temp_data.db")
    engine = create_engine(f"sqlite:///{sqlite_filepath}")
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    # Get the average temperature by date
    date_string = "2019-02-10"
    average_temp = get_average_temp_by_date(date_string, session)
    print(f"Average temp {date_string}: {average_temp:.2f}")
    print()

    # Get the average temps for the year sorted ascending or descending
    average_temps = get_average_temp_sorted("asc", session)
    for row in average_temps:
        print(f"Date: {row.date}, average temp: {row.average_temp:.2f}")
    print()

    print("finished")


if __name__ == "__main__":
    main()
