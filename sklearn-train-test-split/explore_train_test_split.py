import numpy as np
from sklearn.model_selection import train_test_split

x = np.arange(1, 25).reshape(12, 2)
y = np.array([0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0])


x_train, x_test, y_train, y_test = train_test_split(x, y)
print(x_train)
print(x_test)
print(y_train)
print(y_test)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=4, random_state=4
)
# Uncomment to view output
# print(x_train)
# print(x_test)
# print(y_train)
# print(y_test)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.33, random_state=4, stratify=y
)
# Uncomment to view output
# print(x_train)
# print(x_test)
# print(y_train)
# print(y_test)


x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.33, shuffle=False
)
# Uncomment to view output
# print(x_train)
# print(x_test)
# print(y_train)
# print(y_test)
