import datetime

"""
datetime.datetime.now() is preferred over:

- datetime.utc.now()
- datetime.today()
- time.time()
"""

now = datetime.datetime.now()

print(
    f"""
{now=}
{now.time()=}
{now.day=}
{now.isoformat()=}
{now.weekday()=}
{now.isoweekday()=}
{now.isocalendar()=}
{now.hour=}
{now.minute=}
"""
)

# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
print(now.strftime("%A, %B %d %Z"))


# UTC timezone aware object

now = datetime.datetime.now(datetime.timezone.utc)

print(
    f"""
{now=}
{now.isoformat()=}
"""
)

print(now.strftime("%A, %B %d %Z"))


# Local timezone aware object

now = datetime.datetime.now().astimezone()

print(
    f"""
{now=}
{now.isoformat()=}
"""
)

print(now.strftime("%A, %B %d %Z"))


# Alternative local timezone aware object

LOCAL_TIMEZONE = (
    datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
)

now = datetime.datetime.now(LOCAL_TIMEZONE)

print(
    f"""
{now=}
{now.isoformat()=}
"""
)
