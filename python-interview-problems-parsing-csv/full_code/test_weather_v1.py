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
import pytest
import weather_v1 as wthr


@pytest.fixture
def mock_csv_data():
    return [
        "Day,MxT,MnT,AvT,AvDP,1HrP TPcn,PDir,AvSp,Dir,MxS,SkyC,MxR,Mn,R AvSLP",
        "1,88,59,74,53.8,0,280,9.6,270,17,1.6,93,23,1004.5",
        "2,79,63,71,46.5,0,330,8.7,340,23,3.3,70,28,1004.5",
    ]


@pytest.fixture
def mock_csv_file(tmp_path, mock_csv_data):
    datafile = tmp_path / "weather.csv"
    datafile.write_text("\n".join(mock_csv_data))
    return str(datafile)


def test_no_lines():
    no_data = []
    for _ in wthr.get_next_day_and_avg(no_data):
        assert False


def test_trailing_blank_lines(mock_csv_data):
    mock_csv_data.append("")
    all_lines = [x for x in wthr.get_next_day_and_avg(mock_csv_data)]
    assert len(all_lines) == 2
    for line in all_lines:
        assert len(line) == 2


def test_mid_blank_lines(mock_csv_data):
    mock_csv_data.insert(1, "")
    all_lines = [x for x in wthr.get_next_day_and_avg(mock_csv_data)]
    assert len(all_lines) == 2
    for line in all_lines:
        assert len(line) == 2


def test_get_max_avg(mock_csv_file):
    assert wthr.get_max_avg(mock_csv_file) == (1, 73.5)


def test_get_next_day_and_avg(mock_csv_data):
    reader = wthr.get_next_day_and_avg(mock_csv_data)
    assert next(reader) == (1, 73.5)
    assert next(reader) == (2, 71)
    with pytest.raises(StopIteration):
        next(reader)
