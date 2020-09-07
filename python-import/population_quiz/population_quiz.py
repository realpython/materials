# population_quiz.py

import csv
import random

try:
    from importlib import resources
except ImportError:
    import importlib_resources as resources


def read_population_file(year, variant="Medium"):
    """Read population data for the given year and variant"""
    population = {}

    print(f"Reading population data for {year}, {variant} scenario")
    with resources.open_text(
        "data", "WPP2019_TotalPopulationBySex.csv"
    ) as fid:
        rows = csv.DictReader(fid)

        # Read data, filter the correct year
        for row in rows:
            if (
                int(row["LocID"]) < 900
                and row["Time"] == year
                and row["Variant"] == variant
            ):
                pop = round(float(row["PopTotal"]) * 1000)
                population[row["Location"]] = pop

    return population


def run_quiz(population, num_questions, num_countries):
    """Run a quiz about the population of countries"""
    num_correct = 0
    for q_num in range(num_questions):
        print(f"\n\nQuestion {q_num + 1}:")
        countries = random.sample(population.keys(), num_countries)
        print("\n".join(f"{i}. {a}" for i, a in enumerate(countries, start=1)))

        # Get user input
        while True:
            guess_str = input("\nWhich country has the largest population? ")
            try:
                guess_idx = int(guess_str) - 1
                guess = countries[guess_idx]
            except (ValueError, IndexError):
                print(f"Please answer between 1 and {num_countries}")
            else:
                break

        # Check the answer
        correct = max(countries, key=lambda k: population[k])
        if guess == correct:
            num_correct += 1
            print(f"Yes, {guess} is most populous ({population[guess]:,})")
        else:
            print(
                f"No, {correct} ({population[correct]:,}) is more populous "
                f"than {guess} ({population[guess]:,})"
            )

    return num_correct


def main():
    """Read population data and run quiz"""
    population = read_population_file("2020")
    num_correct = run_quiz(population, num_questions=10, num_countries=3)
    print(f"\nYou answered {num_correct} questions correctly")


if __name__ == "__main__":
    main()
