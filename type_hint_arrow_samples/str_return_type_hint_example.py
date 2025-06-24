import random
def get_game_recommendation(list) -> str:
    return random.choice(list)

game_titles_list = ["Dragon Quest", "Final Fantasy", "Age of Empires"]
print(f"Random recommendation: {get_game_recommendation(game_titles_list)}")
