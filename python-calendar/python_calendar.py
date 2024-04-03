import calendar

"""Print full calendar for the year 2024"""

text_calendar = calendar.TextCalendar()
text_calendar.pryear(2024)

"""Print calendar for the month of January 2024"""

text_calendar.prmonth(2024, 1)

"""Generate HTML calendar for 2024 and save to file"""

html_calendar = calendar.HTMLCalendar()
with open("python-calendar.html", mode="wb") as file:
    file.write(html_calendar.formatyearpage(2024))

"""Set first day of the week to Sunday and print January 2024 calendar"""

text_calendar.setfirstweekday(calendar.SUNDAY)
text_calendar.prmonth(2024, 1)

"""Set locale to Germany and print Januar 2024 calendar"""

locale_calendar = calendar.LocaleTextCalendar(locale="de_DE.UTF-8")
locale_calendar.prmonth(2024, 1)

"""Print weekday number values in order with Sunday (6) as the first
day of the week"""

for day_number in text_calendar.iterweekdays():
    print(day_number)

"""Print all dates of January 2024 calendar as strings including dates from
previous and following months needed to complete the first and last weeks"""

for day in text_calendar.itermonthdates(2024, 1):
    day.strftime("%m/%d/%Y")

"""Print all dates of January 2024 calendar as numerical days of the month
including dates from previous and following months needed to complete the
first and last weeks represented as zeros"""

for day in text_calendar.itermonthdays(2024, 1):
    print(day)

"""Print all dates of January 2024 calendar as tuples containing the day of
the month and day of the week as numbers"""

for day in text_calendar.itermonthdays2(2024, 1):
    print(day)

"""Check if a given year is a leap year"""

calendar.isleap(2024)

"""Return the number of leap years between two given years"""

calendar.leapdays(1980, 2024)
