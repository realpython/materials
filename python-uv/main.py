import argparse

import requests

WEATHER_EMOJIS = {
    "clear": "☀️",
    "sunny": "☀️",
    "cloudy": "☁️",
    "partly cloudy": "⛅",
    "rain": "🌧️",
    "light rain": "🌦️",
    "heavy rain": "🌊",
    "storm": "🌩️",
    "snow": "❄️",
    "fog": "🌫️",
    "mist": "🌫️",
    "default": "🌍",
}

API_QUERY_TEMPLATE = "https://wttr.in/{city}?format=%C+%t"


def get_weather_emoji(condition, weather_emojis=WEATHER_EMOJIS):
    condition = condition.lower()
    for key, emoji in weather_emojis.items():
        if key in condition:
            return emoji
    return weather_emojis["default"]


def get_weather(city, api_query_template=API_QUERY_TEMPLATE):
    api_query = api_query_template.format(city=city)
    try:
        response = requests.get(api_query)
        response.raise_for_status()
        weather_info = response.text.strip().split("+")
        if len(weather_info) < 2:
            return "Error: Unexpected weather data format."
        condition = weather_info[0].strip()
        temperature = weather_info[1].strip()
        emoji = get_weather_emoji(condition)
        return f"{emoji} {condition} -> {temperature}"
    except requests.RequestException:
        return "Error: Could not retrieve weather data."


def parse_cli_args():
    parser = argparse.ArgumentParser(
        prog="weather",
        description="Weather information for the specified city.",
        epilog="Thanks for using %(prog)s! :)",
    )
    parser.add_argument(
        "city",
        nargs="+",
        help="Name of the city to get weather information for",
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.0",
    )
    return parser.parse_args()


def main():
    args = parse_cli_args()
    weather = get_weather(" ".join(args.city))
    print(weather)


if __name__ == "__main__":
    main()
