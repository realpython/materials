# flake8: noqa
# 'dataset' holds the input data for this script
dataset[["first_name", "last_name"]] = dataset["full_name"].str.split(
    n=1, expand=True
)
dataset.drop(columns=["full_name"], inplace=True)
