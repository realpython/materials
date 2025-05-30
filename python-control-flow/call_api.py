import os
import random


def main():
    user_key = input("Please enter your API key: ")
    os.environ["API_KEY"] = user_key
    print(f"Temporary API key set: {os.environ['API_KEY']}")

    try:
        run_api_call(os.environ["API_KEY"])
    except Exception as e:
        print(f"Error: {e}")
    else:
        print("API call completed successfully.")
    finally:
        del os.environ["API_KEY"]
        print("API key cleaned up!")


def run_api_call(api_key):
    # Simulate an API call
    if random.choice([True, False]):
        print(f"Running API call with key: {api_key}")
    else:
        raise Exception("API call failed.")


if __name__ == "__main__":
    main()
