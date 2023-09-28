import calendar

sales = {
    calendar.JANUARY: 10,
    calendar.FEBRUARY: 12,
    calendar.MARCH: 8,
    calendar.APRIL: 14,
    calendar.MAY: 16,
    calendar.JUNE: 14,
    calendar.JULY: 21,
    calendar.AUGUST: 22,
    calendar.SEPTEMBER: 20,
    calendar.OCTOBER: 23,
}
for month in calendar.Month:
    if month in sales:
        print(f"{month.value:2d} {month.name:<10} {sales[month]:2d}")
