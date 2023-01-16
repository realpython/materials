#!/usr/bin/env python3
""" Pytest functions for CSV Football problem """
import pytest

# import football_v1 as fb


@pytest.fixture
def mock_csv_data():
    return [
        "Team,Games,Wins,Losses,Draws,Goals For,Goals Against",
        "Liverpool FC, 38, 32, 3, 3, 85, 33",
        "Norwich City FC, 38, 5, 27, 6, 26, 75",
    ]


@pytest.fixture
def mock_csv_file(tmp_path, mock_csv_data):
    datafile = tmp_path / "football.csv"
    datafile.write_text("\n".join(mock_csv_data))
    return str(datafile)
