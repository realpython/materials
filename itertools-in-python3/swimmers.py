from collections import namedtuple
import csv
import datetime
import itertools as it
import statistics


class Event(namedtuple("Event", ["stroke", "name", "time"])):
    __slots__ = ()

    def __lt__(self, other):
        return self.time < other.time


def sort_and_group(iterable, key=None):
    return it.groupby(sorted(iterable, key=key), key=key)


def grouper(iterable, n, fillvalue=None):
    iters = [iter(iterable)] * n
    return it.zip_longest(*iters, fillvalue=fillvalue)


def read_events(csvfile, _strptime=datetime.datetime.strptime):
    def _median(times):
        return statistics.median(
            (_strptime(time, "%M:%S:%f").time() for time in row["Times"])
        )

    fieldnames = ["Event", "Name", "Stroke"]
    with open(csvfile) as infile:
        reader = csv.DictReader(infile, fieldnames=fieldnames, restkey="Times")
        next(reader)  # Skip header.
        for row in reader:
            yield Event(row["Stroke"], row["Name"], _median(row["Times"]))


events = tuple(read_events("swimmers.csv"))

for stroke, evts in sort_and_group(events, key=lambda evt: evt.stroke):
    events_by_name = sort_and_group(evts, key=lambda evt: evt.name)
    best_times = (min(evt) for _, evt in events_by_name)
    sorted_by_time = sorted(best_times, key=lambda evt: evt.time)
    teams = zip(("A", "B"), it.islice(grouper(sorted_by_time, 4), 2))
    for team, swimmers in teams:
        print(
            "{stroke} {team}: {names}".format(
                stroke=stroke.capitalize(),
                team=team,
                names=", ".join(swimmer.name for swimmer in swimmers),
            )
        )
