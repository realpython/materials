"""Offline stand-in for a real weather API client.

It returns canned data, so the CLI works without network access or API keys.
A real provider would live next to this module, for example, `openweather.py`.
"""

CANNED_DAYS = [
    {"date": "Monday", "summary": "Sunny", "low": 12, "high": 21},
    {"date": "Tuesday", "summary": "Partly cloudy", "low": 11, "high": 19},
    {"date": "Wednesday", "summary": "Light rain", "low": 9, "high": 15},
    {"date": "Thursday", "summary": "Windy", "low": 8, "high": 14},
    {"date": "Friday", "summary": "Sunny", "low": 10, "high": 20},
]


class FakeSource:
    def forecast(self, city, days):
        if not 1 <= days <= len(CANNED_DAYS):
            raise LookupError(f"days must be between 1 and {len(CANNED_DAYS)}")
        return {"city": city.title(), "days": CANNED_DAYS[:days]}
