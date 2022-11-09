# flake8: noqa
# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script:

# dataset = pandas.DataFrame(color, vin)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
import matplotlib.pyplot as plt

plt.style.use("seaborn")

series = dataset[dataset["color"] != ""]["color"].value_counts()
series.plot(kind="bar", color=series.index, edgecolor="black")

plt.show()
