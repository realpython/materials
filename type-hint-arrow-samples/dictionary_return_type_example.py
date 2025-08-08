game_stock = {"Dragon Quest": 5, "Final Fantasy": 1, "Age of Empires": 5}


def get_highest_stock_games(game_stock: dict[str, int]) -> dict[str, int]:
    max_quantity = max(game_stock.values())
    return {game: quantity for game, quantity in game_stock.items()
            if quantity == max_quantity}
    
print(f"Games with the highest stock: {get_highest_stock_games(game_stock)}")
