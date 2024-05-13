import datetime


def is_weekday():
    today = datetime.date.today()
    return 0 <= today.weekday() < 5
