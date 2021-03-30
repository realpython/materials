#!/usr/bin/env python3
""" Pytest functions for CSV Football problem """
import pytest
import football_v1 as fb


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


def test_get_min_score(mock_csv_file):
    assert fb.get_min_score_difference(mock_csv_file) == (
        "Norwich City FC",
        49,
    )


def test_parse_next_line(mock_csv_data):
    all_lines = [line for line in fb.parse_next_line(mock_csv_data)]
    assert len(all_lines) == 2
    for line in all_lines:
        assert len(line) == 7


def test_get_score_difference(mock_csv_data):
    reader = fb.parse_next_line(mock_csv_data)
    assert fb.get_name_and_diff(next(reader)) == ("Liverpool FC", 52)
    assert fb.get_name_and_diff(next(reader)) == ("Norwich City FC", 49)
