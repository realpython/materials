import pandas as pd

grades = pd.read_csv(
    "grades.csv",
).convert_dtypes(dtype_backend="pyarrow")

# 1. Use `.dropna()` in such a way that it permanently drops the row in the dataframe containing only null values.

grades.dropna(how="all", inplace=True)

# 2. Display the rows for the exams that all students have completed.

grades.dropna()

# 3. Display any columns with no missing data.

grades.dropna(axis=1)

# 4. Display the exams sat by at least five students.

grades.dropna(axis=0, thresh=6)  # Remember there are seven columns.

# 5. Who else was in in every exam that both S2 and S4 sat?

grades.dropna(subset=["S2", "S4"]).dropna(axis=1, ignore_index=True)
