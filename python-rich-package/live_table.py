import contextlib
import json
import time
from pathlib import Path

from rich.console import Console
from rich.live import Live
from rich.table import Table

console = Console()


def make_table(coin_list):
    """Generate a rich table from a list of coins"""
    table = Table(
        title=f"Crypto Data - {time.asctime()}",
        style="black on grey66",
        header_style="white on dark_blue",
    )
    table.add_column("Symbol")
    table.add_column("Name", width=30)
    table.add_column("Price (USD)", justify="right")
    table.add_column("Volume (24h)", justify="right", width=16)
    table.add_column("Percent Change (7d)", justify="right", width=8)
    for coin in coin_list:
        symbol, name, price, volume, pct_change = (
            coin["symbol"],
            coin["name"],
            coin["price_usd"],
            f"{coin['volume24']:.2f}",
            float(coin["percent_change_7d"]),
        )
        pct_change_str = f"{pct_change:2.1f}%"
        if pct_change > 5.0:
            pct_change_str = f"[white on dark_green]{pct_change_str:>8}[/]"
        elif pct_change < -5.0:
            pct_change_str = f"[white on red]{pct_change_str:>8}[/]"
        table.add_row(symbol, name, price, volume, pct_change_str)
    return table


# Load the coins data
raw_data = json.loads(Path("crypto_data.json").read_text(encoding="utf-8"))
num_coins = len(raw_data)
coins = raw_data + raw_data  # Double the dataset to simulate streaming


def display_table(nlines):
    """Display a scrolling table with `nlines` lines"""
    with Live(make_table(coins[:nlines]), screen=True) as live:
        index = 0
        with contextlib.suppress(KeyboardInterrupt):
            while True:
                live.update(make_table(coins[index : index + nlines]))
                time.sleep(0.5)
                index = (index + 1) % num_coins


if __name__ == "__main__":
    import sys

    NLINES = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    display_table(NLINES)
