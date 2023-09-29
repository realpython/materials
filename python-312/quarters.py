import calendar
import itertools

for quarter in itertools.batched(calendar.Month, n=3):
    print([month.name for month in quarter])
