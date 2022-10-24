# flake8: noqa
# 'dataset' holds the input data for this script
dataset = dataset.assign(
    full_name=dataset["customer"].str.extract(r"([^<]+)"),
    email=dataset["customer"].str.extract(r"<([^>]+)>"),
).drop(columns=["customer"])
