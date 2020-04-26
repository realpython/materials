"""
Constrained minimization example code using SciPy.

Associated with the Real Python article
Scientific Python: Using SciPy for Optimization
Available at: https://realpython.com/python-scipy-cluster-optimize/
"""
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
print("Leftover money for each buyer:", money_available - res.x * prices)
