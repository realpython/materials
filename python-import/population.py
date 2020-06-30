# population.py

import csv
from importlib import resources

import matplotlib.pyplot as plt


class _Population:
    def __init__(self):
        """Prepare to read the population file"""
        self._data = {}
        self.variant = "Medium"

    @property
    def data(self):
        """Read data from disk"""
        if self._data:  # Data has already been read, return it directly
            return self._data

        # Read data and store it in self._data
        print(f"Reading population data for {self.variant} scenario")
        with resources.open_text(
            "data", "WPP2019_TotalPopulationBySex.csv"
        ) as fid:
            rows = csv.DictReader(fid)

            # Read data, filter the correct variant
            for row in rows:
                if int(row["LocID"]) >= 900 or row["Variant"] != self.variant:
                    continue

                country = self._data.setdefault(row["Location"], {})
                population = float(row["PopTotal"]) * 1000
                country[int(row["Time"])] = round(population)
        return self._data

    def get_country(self, country):
        """Get population data for one country"""
        country = self.data[country]
        years, population = zip(*country.items())
        return years, population

    def plot_country(self, country):
        """Plot data for one country, population in millions"""
        years, population = self.get_country(country)
        plt.plot(years, [p / 1e6 for p in population], label=country)

    def order_countries(self, year):
        """Sort countries by population in decreasing order"""
        countries = {c: self.data[c][year] for c in self.data}
        return sorted(countries, key=lambda c: countries[c], reverse=True)


# Instantiate the singleton
data = _Population()
