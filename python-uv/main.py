import argparse
import sys

import requests


def get_breeds_info():
    response = requests.get("https://api.thecatapi.com/v1/breeds")
    response.raise_for_status()
    return response.json()


def find_breed_info(breed_name):
    json_response = get_breeds_info()
    for breed in json_response:
        if breed["name"] == breed_name:
            return breed
    return None


def display_breed_profile(breed):
    print(f"\n{breed['name']:-^30s}")
    print(f"Origin: {breed['origin']}")
    print(f"Temperament: {breed['temperament']}")
    print(f"Life Span: {breed['life_span']} years")
    print(f"Weight: {breed['weight']['imperial']} lbs")
    if breed.get("wikipedia_url"):
        print(f"\nLearn more: {breed['wikipedia_url']}")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Get information about cat breeds",
    )
    parser.add_argument(
        "breed",
        help="Name of cat breed (e.g., 'Siamese')",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    try:
        breed = find_breed_info(args.breed)
        if not breed:
            print("Breed not found. Try another breed name.")
            return 0
        display_breed_profile(breed)
    except Exception as e:
        print(f"Error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
