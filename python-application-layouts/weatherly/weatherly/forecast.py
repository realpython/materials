from weatherly.sources import get_source


def fetch_forecast(city, days=3, source="fake"):
    """Fetch a forecast for city from the given source."""
    client = get_source(source)
    return client.forecast(city, days)


def format_forecast(forecast):
    """Format a forecast as human-readable lines of text."""
    lines = [f"Forecast for {forecast['city']}:"]
    for day in forecast["days"]:
        lines.append(
            f"  {day['date']}: {day['summary']}, "
            f"{day['low']}°C to {day['high']}°C"
        )
    return "\n".join(lines)
