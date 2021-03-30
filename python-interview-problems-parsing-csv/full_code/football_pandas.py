import pandas as pd


def read_data(csv_file):
    return (
        pd.read_csv(csv_file)
        .rename(
            columns={
                "Team": "team_name",
                "Goals For": "goals",
                "Goals Against": "goals_allowed",
            }
        )
        .assign(goal_difference=lambda df: abs(df.goals - df.goals_allowed))
    )


def get_min_difference(parsed_data):
    return parsed_data.goal_difference.min()


def get_team(parsed_data, min_score_difference):
    return (
        parsed_data.query(f"goal_difference == {min_score_difference}")
        .reset_index()
        .loc[0, "team_name"]
    )


def get_min_score_difference(csv_file):
    df = read_data(csv_file)
    min_diff = get_min_difference(df)
    team = get_team(df, min_diff)
    return team, min_diff
