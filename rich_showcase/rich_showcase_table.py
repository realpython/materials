#!/usr/bin/env python
# coding: utf-8

"""Sample code for Rich showcase article"""

import time
from rich.table import Table
from rich.live import Live
from rich.console import Console
from rich_showcase_data import DEMO_DATA


def make_table(coin_list):
    """Generate a rich table from a list of coins"""
    table = Table(
        title="Crypto Data - " + time.asctime(),
        style="black on grey66",
        header_style="white on dark_blue",
    )
    table.add_column("Symbol")
    table.add_column("Name", width=30)
    table.add_column("Price (USD)", justify="right")
    table.add_column("Volume (24h)", justify="right")
    table.add_column("Percent Change (7d)", justify="right", width=8)
    for coin in coin_list:
        symbol, name, price, volume = (
            coin["symbol"],
            coin["name"],
            str(coin["price_usd"]),
            str(coin["volume24"]),
        )
        pct_change = float(coin["percent_change_7d"])
        pct_change_str = f"{pct_change:2.1f}%"
        if pct_change > 5.0:
            pct_change_str = (
                f"[white on dark_green]{pct_change_str:>8}[/white on dark_green]"
            )
        elif pct_change < -5.0:
            pct_change_str = f"[white on red]{pct_change_str:>8}[/white on red]"
        table.add_row(symbol, name, price, volume, pct_change_str)
    return table


coins = DEMO_DATA
console = Console()


def display_table(nlines):
    """Display a scrolling table with `nlines` lines"""
    with Live(make_table(coins[:nlines]), screen=True) as live:
        index = 0
        try:
            while True:
                overlap = nlines - (len(coins) - index)
                if overlap <= 0:
                    lines = coins[index : index + nlines]
                else:
                    lines = coins[index:] + coins[:overlap]
                live.update(make_table(lines))
                time.sleep(0.5)
                index = (index + 1) % len(coins)
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        NLINES = int(sys.argv[1])
    else:
        NLINES = 20
    display_table(NLINES)
