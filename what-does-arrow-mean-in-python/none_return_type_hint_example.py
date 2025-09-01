def find_keyword_in_titles(titles: list[str], keyword: str) -> None:
    print("Titles that contain the keyword:", keyword)
    for game_title in titles:
        if keyword in game_title:
            print(game_title)


games = ["Dragon Quest", "Final Fantasy", "Age of Empires"]
find_keyword_in_titles(games, "es")
