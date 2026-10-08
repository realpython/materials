import pandas

df = pandas.read_csv(
    "hrdata.csv",
    index_col="Employee",
    parse_dates=["Hired"],
    date_format="%m/%d/%y",
    header=0,
    names=["Employee", "Hired", "Salary", "Sick Days"],
)
df.to_csv("hrdata_modified.csv")
