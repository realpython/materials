import sys

import yfinance as yf

TICKERS = ["AAPL", "JPM", "XOM", "JNJ", "SPY"]

prices = yf.download(
    TICKERS, start="2021-01-01", end="2026-01-01", progress=False
)["Close"]
prices = prices.reindex(columns=TICKERS)
failed = prices.columns[prices.isna().all()].tolist()
if failed:
    sys.exit(f"Download failed for {', '.join(failed)}")
prices.to_csv("prices.csv")
print(prices.tail())
