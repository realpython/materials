import pytest
import football_pandas as fb


@pytest.fixture
def mock_csv_file(tmp_path):
    mock_csv_data = [
        "Team,Games,Wins,Losses,Draws,Goals For,Goals Against",
        "Liverpool FC, 38, 32, 3, 3, 85, 33",
        "Norwich City FC, 38, 5, 27, 6, 26, 75",
    ]
    datafile = tmp_path / "football.csv"
    datafile.write_text("\n".join(mock_csv_data))
    return str(datafile)


def test_read_data(mock_csv_file):
    df = fb.read_data(mock_csv_file)
    rows, cols = df.shape
    assert rows == 2
    # The dataframe df has all seven of the cols in the original dataset plus
    # the goal_difference col added in read_data().
    assert cols == 8


def test_score_difference(mock_csv_file):
    df = fb.read_data(mock_csv_file)
    assert df.team_name[0] == "Liverpool FC"
    assert df.goal_difference[0] == 52
    assert df.team_name[1] == "Norwich City FC"
    assert df.goal_difference[1] == 49


def test_get_min_diff(mock_csv_file):
    df = fb.read_data(mock_csv_file)
    diff = fb.get_min_difference(df)
    assert diff == 49


def test_get_team_name(mock_csv_file):
    df = fb.read_data(mock_csv_file)
    assert fb.get_team(df, 49) == "Norwich City FC"
    assert fb.get_team(df, 52) == "Liverpool FC"


def test_get_min_score(mock_csv_file):
    assert fb.get_min_score_difference(mock_csv_file) == (
        "Norwich City FC",
        49,
    )
