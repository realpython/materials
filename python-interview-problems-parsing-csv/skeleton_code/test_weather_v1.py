#!/usr/bin/env python3
""" Pytest functions for CSV Weather problem """
import pytest

# import weather_v1 as wthr


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
