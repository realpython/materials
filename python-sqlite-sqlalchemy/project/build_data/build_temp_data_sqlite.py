"""
This program gathers information from the temp_data.db file about temperature
"""

import os
import csv
from pkg_resources import resource_filename
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class TemperatureData(Base):
    __tablename__ = "temperature_data"
    temperature_data_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    value = Column(Float, nullable=False)


def get_temperature_data(filepath):
    """
    This function gets the temperature data from the csv file
    """
    with open(filepath) as csvfile:
        csv_reader = csv.DictReader(csvfile)
        data = {row["name"]: row for row in csv_reader}
        for value in data.values():
            value.pop("name")
        return data


def populate_database(session, temperature_data):
    # insert the data
    for student, data in temperature_data.items():
        for date, value in data.items():
            temp_data = TemperatureData(
                name=student,
                date=datetime.strptime(date, "%Y-%m-%d").date(),
                value=value,
            )
            session.add(temp_data)
        session.commit()
    session.close()


def main():
    print("starting")

    # get the temperature data into a dictionary structure
    csv_filepath = resource_filename("project.data", "temp_data.csv")
    temperature_data = get_temperature_data(csv_filepath)

    # get the filepath to the database file
    sqlite_filepath = resource_filename("project.data", "temp_data.db")

    # does the database exist?
    if os.path.exists(sqlite_filepath):
        os.remove(sqlite_filepath)

    # create and populate the sqlite database
    engine = create_engine(f"sqlite:///{sqlite_filepath}")
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    populate_database(session, temperature_data)

    print("finished")


if __name__ == "__main__":
    main()
