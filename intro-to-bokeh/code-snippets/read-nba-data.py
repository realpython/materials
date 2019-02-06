import pandas as pd

# Read the csv files
player_stats = pd.read_csv(
    "2017-18_playerBoxScore.csv", parse_dates=["gmDate"]
)
team_stats = pd.read_csv("2017-18_teamBoxScore.csv", parse_dates=["gmDate"])
standings = pd.read_csv("2017-18_standings.csv", parse_dates=["stDate"])


# Prepare the DataFrames used throughout the tutorial

####################################################################
# west_top_2: Used in Using the ColumnDataSource Object

west_top_2 = (
    standings[
        (standings["teamAbbr"] == "HOU") | (standings["teamAbbr"] == "GS")
    ]
    .loc[:, ["stDate", "teamAbbr", "gameWon"]]
    .sort_values(["teamAbbr", "stDate"])
)

####################################################################
# three_takers: Used in Selecting Data Points

# Find players who took at least 1 three-point shot during the season
three_takers = player_stats[player_stats["play3PA"] > 0]

# Clean up the player names, placing them in a single column
three_takers["name"] = [
    f'{p["playFNm"]} {p["playLNm"]}' for _, p in three_takers.iterrows()
]

# Aggregate the total three-point attempts and makes for each player
three_takers = (
    three_takers.groupby("name")
    .sum()
    .loc[:, ["play3PA", "play3PM"]]
    .sort_values("play3PA", ascending=False)
)

# Filter out anyone who didn't take at least 100 three-point shots
three_takers = three_takers[three_takers["play3PA"] >= 100].reset_index()

# Add a column with a calculated three-point percentage (made/attempted)
three_takers["pct3PM"] = three_takers["play3PM"] / three_takers["play3PA"]


####################################################################
# phi_gm_stats: Used in Linking Axes and Selections

# Isolate relevant data
phi_gm_stats = (
    team_stats[
        (team_stats["teamAbbr"] == "PHI")
        & (team_stats["seasTyp"] == "Regular")
    ]
    .loc[:, ["gmDate", "teamPTS", "teamTRB", "teamAST", "teamTO", "opptPTS"]]
    .sort_values("gmDate")
)

# Add game number
phi_gm_stats["game_num"] = range(1, len(phi_gm_stats) + 1)

# Derive a win_loss column
win_loss = []
for _, row in phi_gm_stats.iterrows():

    # If the 76ers score more points, it's a win
    if row["teamPTS"] > row["opptPTS"]:
        win_loss.append("W")
    else:
        win_loss.append("L")

# Add the win_loss data to the DataFrame
phi_gm_stats["winLoss"] = win_loss

####################################################################
# phi_gm_stats_2: Used in Linking Axes and Selections

# Isolate relevant data
phi_gm_stats_2 = (
    team_stats[
        (team_stats["teamAbbr"] == "PHI")
        & (team_stats["seasTyp"] == "Regular")
    ]
    .loc[:, ["gmDate", "team2P%", "team3P%", "teamPTS", "opptPTS"]]
    .sort_values("gmDate")
)

# Add game number
phi_gm_stats_2["game_num"] = range(1, len(phi_gm_stats_2) + 1)

# Derive a win_loss column
win_loss = []
for _, row in phi_gm_stats_2.iterrows():

    # If the 76ers score more points, it's a win
    if row["teamPTS"] > row["opptPTS"]:
        win_loss.append("W")
    else:
        win_loss.append("L")

# Add the win_loss data to the DataFrame
phi_gm_stats_2["winLoss"] = win_loss
