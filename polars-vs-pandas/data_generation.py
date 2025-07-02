import numpy as np


def data_generation(number_of_rows):
    return {
        "order_id": range(1, number_of_rows + 1),
        "region": np.random.choice(
            ["North", "South", "East", "West"], size=number_of_rows
        ),
        "sales_person": np.random.choice(
            ["Armstrong", "Aldrin", "Collins"], size=number_of_rows
        ),
        "product": np.random.choice(
            ["Helmet", "Oxygen", "Boots", "Gloves"], size=number_of_rows
        ),
        "sales_income": np.random.randint(1, 5001, size=number_of_rows),
    }
