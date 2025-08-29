import random


def get_game_recommendation(titles: list[str]) -> str:
    return random.choice(titles)


games = ["Dragon Quest", "Final Fantasy", "Age of Empires"]
print("Random recommendation:", get_game_recommendation(games))
