import datetime


def day_number(date_to_convert: datetime.date):
    """
    >>> day_number(datetime.date(2022,1,1))
    1
    >>> day_number(datetime.date(2022,12,31))
    365
    """
    return (
        date_to_convert - datetime.date(date_to_convert.year, 1, 1)
    ).days + 1
