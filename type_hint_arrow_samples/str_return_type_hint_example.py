import random


def get_game_recommendation(titles: list) -> str:
    return random.choice(titles)


game_titles_list = ["Dragon Quest", "Final Fantasy", "Age of Empires"]
print(f"Random recommendation: {get_game_recommendation(game_titles_list)}")
