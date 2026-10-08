# Python for Stock Analysis: Build a Portfolio Analyzer

This folder provides the code examples for the Real Python tutorial [Python for Stock Analysis: Build a Portfolio Analyzer](https://realpython.com/python-stock-portfolio-analysis/).

- `fetch_prices.py`: Downloads adjusted daily closing prices with yfinance and saves them to `prices.csv`
- `prices.csv`: Snapshot of the prices used in the tutorial (2021-01-04 to 2025-12-31, downloaded in October 2026)
- `portfolio.py`: The finished portfolio analyzer

Install the dependencies with `python -m pip install -r requirements.txt`, then run `python portfolio.py` to print the summary table and save `growth.png`.
