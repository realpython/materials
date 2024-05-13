import pandas as pd

# Read the CSV data into a pandas dataframe
companies = pd.read_csv("companies.csv")

# Check the size of the dataframe
print(companies.shape)

# Inspect the first 5 rows of the dataframe
print(companies.head())

# Filter for rows where the company slogan contains the word "secret"
print(companies[companies.slogan.str.contains("secret")])

# Apply a regex pattern to the string search to narrow the results
print(companies[companies.slogan.str.contains(r"secret\w+")])
