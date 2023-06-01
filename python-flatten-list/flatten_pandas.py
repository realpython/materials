import pandas as pd

matrix = [list(range(100))] * 4
df = pd.DataFrame(matrix)


def flatten_pandas(matrix):
    return pd.DataFrame(matrix.to_numpy().flatten())
