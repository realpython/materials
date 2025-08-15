import numpy as np


def generate_data(number_of_rows):
    rng = np.random.default_rng()

    return {
        "order_id": range(1, number_of_rows + 1),
        "region": rng.choice(["North", "South", "East", "West"], size=number_of_rows),
        "sales_person": rng.choice(
            ["Armstrong", "Aldrin", "Collins"], size=number_of_rows
        ),
        "product": rng.choice(
            ["Helmet", "Oxygen", "Boots", "Gloves"], size=number_of_rows
        ),
        "sales_income": rng.integers(1, 5001, size=number_of_rows),
    }
