def find_keyword_in_titles(list, keyword) -> None:
    print(f"Titles that contain the keyword {keyword}")
    for game_title in list:
        if keyword in game_title:
            print(f"{game_title}")

game_titles_list = ["Dragon Quest", "Final Fantasy", "Age of Empires"]
find_keyword_in_titles(game_titles_list, "Final")  