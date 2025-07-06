game_stock = {"Dragon Quest": 5, "Final Fantasy": 1, "Age of Empires": 5}


def get_highest_stock_game() -> dict[str, int]:
    stock_quantities = game_stock.values()
    high = 0
    for quantity in stock_quantities:
        if quantity > high:
            high = quantity
    game_results = {}

    for game in game_stock:
        if game_stock[game] == high:
            game_results[game] = high
    return game_results


print(f"Games with the highest stock: {get_highest_stock_game()}")
