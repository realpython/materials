grades = pd.read_csv(
    "grades.csv",
).convert_dtypes(dtype_backend="pyarrow")

# 1. Permanently drop the last row of the dataframe.

grades.dropna(how="all", inplace=True)

# 2. Display the rows for the exams that all students have completed.

grades.dropna()

# 3. Display any columns with no missing data.

grades.dropna(axis=1)

# 4. Display the exams students have sat five or more times.

grades.dropna(axis=0, thresh=6)  # Remember there are seven columns.

# 5. Who else would be in the exam hall when both `S2` and `S4` were there?

grades.dropna(subset=["S2", "S4"]).dropna(axis=1, ignore_index=True)
