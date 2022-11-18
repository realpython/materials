import numpy as np
from colorama import Cursor

grid = np.array(
    [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1],
        [1, 0, 0, 2, 1],
        [1, 1, 1, 1, 1],
    ]
)

num_rows, num_cols = grid.shape
for row in range(num_rows):
    for col in range(num_cols):
        symbol = " *o"[grid[row, col]]
        print(f"{Cursor.POS(col + 1, row + 2)}{symbol}")
