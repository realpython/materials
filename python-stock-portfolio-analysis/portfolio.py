import matplotlib.pyplot as plt
import pandas as pd

TRADING_DAYS = 252
WEIGHTS = {"AAPL": 0.4, "JPM": 0.2, "XOM": 0.2, "JNJ": 0.2}
BENCHMARK = "SPY"


def load_prices(path="prices.csv"):
    return pd.read_csv(path, index_col="Date", parse_dates=True)


def calculate_returns(prices):
    if prices.isna().any().any():
        raise ValueError("Found missing prices. Choose dates without gaps.")
    if len(prices) < 3:
        raise ValueError("You need at least three days of prices.")
    return prices.pct_change().iloc[1:]


def build_portfolio(returns, weights):
    weights = pd.Series(weights)
    if not (weights >= 0).all() or abs(weights.sum() - 1) > 1e-9:
        raise ValueError("Weights must be non-negative and add up to 1.")
    holdings = returns[weights.index]
    return holdings @ weights


def growth_of(returns, initial=10_000):
    return initial * (1 + returns).cumprod()


def annualized_return(returns):
    years = len(returns) / TRADING_DAYS
    return (1 + returns).prod() ** (1 / years) - 1


def annualized_volatility(returns):
    return returns.std() * TRADING_DAYS**0.5


def drawdowns(returns):
    growth = (1 + returns).cumprod()
    peak = growth.cummax().clip(lower=1)
    return growth / peak - 1


def max_drawdown(returns):
    return drawdowns(returns).min()


def sharpe_ratio(returns, risk_free_rate=0.0):
    daily_risk_free = (1 + risk_free_rate) ** (1 / TRADING_DAYS) - 1
    excess = returns - daily_risk_free
    if excess.std() == 0:
        return float("nan")
    return excess.mean() / excess.std() * TRADING_DAYS**0.5


def summarize(returns, risk_free_rate=0.0):
    sharpe = returns.apply(sharpe_ratio, risk_free_rate=risk_free_rate)
    return pd.DataFrame(
        {
            "Return": returns.apply(annualized_return),
            "Volatility": returns.apply(annualized_volatility),
            "Max Drawdown": returns.apply(max_drawdown),
            "Sharpe": sharpe,
        }
    )


def plot_growth(returns, filename="growth.png"):
    fig, (top, bottom) = plt.subplots(
        2, 1, figsize=(10, 7), sharex=True, height_ratios=[3, 1]
    )
    growth_of(returns).plot(ax=top, title="Growth of $10,000")
    drawdowns(returns).plot(ax=bottom, title="Drawdown", legend=False)
    top.yaxis.set_major_formatter("${x:,.0f}")
    bottom.yaxis.set_major_formatter("{x:.0%}")
    fig.tight_layout()
    fig.savefig(filename)


if __name__ == "__main__":
    prices = load_prices()
    returns = calculate_returns(prices)
    returns["Portfolio"] = build_portfolio(returns, WEIGHTS)
    comparison = returns[["Portfolio", BENCHMARK]]
    print(summarize(comparison, risk_free_rate=0.03).round(3))
    plot_growth(comparison)
