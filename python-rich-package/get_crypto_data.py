import requests

COINLORE_API = "https://api.coinlore.net/api/tickers/"
KEYS = frozenset(
    ("symbol", "name", "price_usd", "volume24", "percent_change_7d")
)


def fetch_coin_data(n_coins=100, keys=KEYS):
    """Get sample data from the CoinLore API

    @param n_coins: number of coins to get data for
    @param keys: subset of keys to keep for each coin
    @return: list of dictionaries containing data for each coin
    """
    url = f"{COINLORE_API}?limit={n_coins}"
    resp = requests.get(url, timeout=5)

    return [
        {k: v for k, v in d.items() if k in keys} for d in resp.json()["data"]
    ]


if __name__ == "__main__":
    print(fetch_coin_data())
