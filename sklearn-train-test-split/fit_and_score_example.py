import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

x = np.arange(20).reshape(-1, 1)
y = np.array(
    [
        5,
        12,
        11,
        19,
        30,
        29,
        23,
        40,
        51,
        54,
        74,
        62,
        68,
        73,
        89,
        84,
        89,
        101,
        99,
        106,
    ]
)


x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=8, random_state=0
)

model = LinearRegression().fit(x_train, y_train)
print(model.intercept_)
print(model.coef_)

print(model.score(x_train, y_train))
print(model.score(x_test, y_test))
