import pandas

df = pandas.read_csv("hrdata.csv")
print(df)

print(type(df["Hire Date"][0]))

df = pandas.read_csv("hrdata.csv", index_col="Name")
print(df)

df = pandas.read_csv(
    "hrdata.csv",
    index_col="Name",
    parse_dates=["Hire Date"],
    date_format="%m/%d/%y",
)
print(df)

print(type(df["Hire Date"].iloc[0]))

df = pandas.read_csv(
    "hrdata.csv",
    index_col="Employee",
    parse_dates=["Hired"],
    date_format="%m/%d/%y",
    header=0,
    names=["Employee", "Hired", "Salary", "Sick Days"],
)
print(df)
