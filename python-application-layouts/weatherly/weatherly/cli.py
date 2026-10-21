import argparse

from weatherly.forecast import fetch_forecast, format_forecast


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="weatherly", description="Show the weather forecast for a city."
    )
    parser.add_argument("city", help="name of the city")
    parser.add_argument(
        "-d",
        "--days",
        type=int,
        default=3,
        help="number of days to show (default: 3)",
    )
    args = parser.parse_args(argv)
    try:
        forecast = fetch_forecast(args.city, days=args.days)
    except LookupError as error:
        parser.exit(1, f"weatherly: {error}\n")
    print(format_forecast(forecast))
