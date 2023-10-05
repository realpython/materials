import calendar

sales = {
    calendar.JANUARY: 5,
    calendar.FEBRUARY: 9,
    calendar.MARCH: 6,
    calendar.APRIL: 14,
    calendar.MAY: 9,
    calendar.JUNE: 8,
    calendar.JULY: 15,
    calendar.AUGUST: 22,
    calendar.SEPTEMBER: 20,
    calendar.OCTOBER: 23,
}
for month in calendar.Month:
    if month in sales:
        print(
            f"{month.value:2d} {month.name:<10}"
            f" {sales[month]:2d} {'*' * sales[month]}"
        )
