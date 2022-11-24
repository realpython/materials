from datetime import datetime


def main():
    inverse(0)


def inverse(number):
    return 1 / number


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        err.add_note(f"Raised at {datetime.now()}")
        raise
