import random

def get_game_recommendations(titles: list) -> str:
    return random.choice(titles)

game_titles_list = ["Dragon Quest", "Final Fantasy", "Age of Empires"]
print(f"Random recommendation: {get_game_redommendation(game_titles_list)}")
