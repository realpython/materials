from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

x, y = fetch_california_housing(return_X_y=True)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.4, random_state=0
)


model = LinearRegression().fit(x_train, y_train)
print("LinearRegression:")
print(model.score(x_train, y_train))
print(model.score(x_test, y_test), end="\n\n")

model = GradientBoostingRegressor(random_state=0).fit(x_train, y_train)
print("GradientBoostingRegressor:")
print(model.score(x_train, y_train))
print(model.score(x_test, y_test), end="\n\n")

model = RandomForestRegressor(random_state=0).fit(x_train, y_train)
print("RandomForestRegressor:")
print(model.score(x_train, y_train))
print(model.score(x_test, y_test), end="\n\n")
