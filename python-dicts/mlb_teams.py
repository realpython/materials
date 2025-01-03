MLB_teams = {
    "Colorado": "Rockies",
    # "Chicago": "White Sox",
    "Chicago": "Chicago Cubs",
    "Boston": "Red Sox",
    "Minnesota": "Twins",
    "Milwaukee": "Brewers",
    "Seattle": "Mariners",
}
print(MLB_teams)

MLB_teams = dict(
    [
        ("Colorado", "Rockies"),
        ("Chicago", "White Sox"),
        ("Boston", "Red Sox"),
        ("Minnesota", "Twins"),
        ("Milwaukee", "Brewers"),
        ("Seattle", "Mariners"),
    ]
)
print(MLB_teams)


print("Milwaukee" in MLB_teams)
print("Indianapolis" in MLB_teams)
print("Indianapolis" not in MLB_teams)
print("Milwaukee" in MLB_teams.keys())
print("Indianapolis" in MLB_teams.keys())
print("Indianapolis" not in MLB_teams.keys())

print(("Boston", "Red Sox") in MLB_teams.items())
print(("Boston", "Red Sox") not in MLB_teams.items())
