from datetime import datetime


def days_to_snake_day(from_date=None):
    """Return the number of days until World Snake Day (July 16th)."""
    if from_date is None:
        from_date = datetime.now()
    if from_date.month > 7 or (from_date.month == 7 and from_date.day > 16):
        day_of_snake = datetime(from_date.year + 1, 7, 16)
    else:
        day_of_snake = datetime(from_date.year, 7, 16)
    return (day_of_snake - from_date).days
