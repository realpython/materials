import yfinance as yf

TICKERS = ["AAPL", "JPM", "XOM", "JNJ", "SPY"]

prices = yf.download(
    TICKERS, start="2021-01-01", end="2026-01-01", progress=False
)["Close"]
prices = prices[TICKERS].round(2)
prices.to_csv("prices.csv")
print(prices.tail())
