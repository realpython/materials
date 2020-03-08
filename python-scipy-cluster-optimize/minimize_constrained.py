import numpy as np
from scipy.optimize import minimize, LinearConstraint

n_buyers = 10
n_shares = 15
np.random.seed(10)
prices = np.random.random(n_buyers)
money_available = np.random.randint(1, 4, n_buyers)
n_shares_per_buyer = money_available / prices
print(prices, money_available, n_shares_per_buyer, sep="\n")
constraint = LinearConstraint(np.ones(n_buyers), lb=n_shares, ub=n_shares)
bounds = [(0, n) for n in n_shares_per_buyer]


def objective_function(x, prices):
    return -x.dot(prices)


res = minimize(
    objective_function,
    10 * np.random.random(n_buyers),
    args=(prices,),
    constraints=constraint,
    bounds=bounds,
)
print(res)

print("The total number of shares is:", sum(res.x))
print("The cash each buyer has leftover is:", money_available - res.x * prices)
