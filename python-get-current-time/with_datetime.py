from datetime import datetime, timezone

"""
datetime.datetime.now() is preferred over:

- datetime.utc.now()
- datetime.today()
- time.time()
"""

now = datetime.now()

print(
    f"""
{now = }
{now.time()         = }
{now.day            = }
{now.hour           = }
{now.minute         = }
{now.isoformat()    = }
{now.weekday()      = }
{now.isoweekday()   = }
{now.isocalendar()  = }

"""
)

# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
print(now.strftime("%A, %B %d %Z"))


# UTC timezone aware object

now = datetime.now(timezone.utc)

print(
    f"""
UTC timezone aware:
{now = }
{now.isoformat() = }
"""
)

print(now.strftime("%A, %B %d %Z"))
