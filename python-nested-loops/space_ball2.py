players = ["Bonnie", "Mike", "Raj", "Adah"]

for player1 in players:
    for player2 in players:
        if player1 != player2:
            print(f"{player1} vs {player2}")
