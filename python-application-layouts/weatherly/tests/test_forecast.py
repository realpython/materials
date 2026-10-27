import pytest

from weatherly.forecast import fetch_forecast, format_forecast


def test_fetch_forecast_returns_requested_days():
    forecast = fetch_forecast("berlin", days=2)
    assert forecast["city"] == "Berlin"
    assert len(forecast["days"]) == 2


def test_fetch_forecast_rejects_unknown_source():
    with pytest.raises(LookupError):
        fetch_forecast("berlin", source="nowhere")


def test_format_forecast():
    forecast = {
        "city": "Berlin",
        "days": [
            {"date": "Monday", "summary": "Sunny", "low": 12, "high": 21}
        ],
    }
    assert format_forecast(forecast) == (
        "Forecast for Berlin:\n  Monday: Sunny, 12°C to 21°C"
    )
