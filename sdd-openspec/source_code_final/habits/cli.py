import argparse
import os
import sys
from datetime import date, timedelta

from habits import storage


def iso_date(value):
    try:
        return date.fromisoformat(value)
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"invalid date '{value}', expected YYYY-MM-DD"
        ) from None


def main(argv=None):
    parser = argparse.ArgumentParser(prog="habits")
    commands = parser.add_subparsers(dest="command", required=True)

    add = commands.add_parser("add", help="start tracking a new habit")
    add.add_argument("name")

    done = commands.add_parser("done", help="check in a habit")
    done.add_argument("name")
    when = done.add_mutually_exclusive_group()
    when.add_argument("--yesterday", action="store_true")
    when.add_argument(
        "--date",
        type=iso_date,
        metavar="YYYY-MM-DD",
        help="check in for this day",
    )

    commands.add_parser("list", help="show all habits and their streaks")
    commands.add_parser("stats", help="show streaks and totals for each habit")

    args = parser.parse_args(argv)
    path = os.environ.get("HABITS_FILE", storage.DEFAULT_PATH)
    tracker = storage.load(path)

    try:
        if args.command == "add":
            tracker.add(args.name)
            print(f"Tracking '{args.name}'.")
        elif args.command == "done":
            today = date.today()
            if args.date is not None:
                day = args.date
            elif args.yesterday:
                day = today - timedelta(days=1)
            else:
                day = today
            tracker.check_in(args.name, day, today=today)
            streak = tracker.streak(args.name, today=today)
            if day != today:
                print(f"Checked in '{args.name}' for {day}. Streak: {streak}")
            else:
                print(f"Checked in '{args.name}'. Streak: {streak}")
        elif args.command == "list":
            for habit in tracker.habits.values():
                print(
                    f"{habit.name:<20} {tracker.streak(habit.name):>3} day(s)"
                )
        elif args.command == "stats":
            print_stats(tracker)
            return 0
    except (KeyError, ValueError) as error:
        print(f"Error: {error.args[0]}", file=sys.stderr)
        return 1

    storage.save(tracker, path)
    return 0


def print_stats(tracker):
    if not tracker.habits:
        print("No habits yet. Add one with 'habits add <name>'.")
        return
    print(f"{'Habit':<20} {'Current':>7} {'Longest':>7} {'Total':>5}")
    for habit in tracker.habits.values():
        print(
            f"{habit.name:<20}"
            f" {tracker.streak(habit.name):>7}"
            f" {tracker.longest_streak(habit.name):>7}"
            f" {tracker.total_check_ins(habit.name):>5}"
        )


if __name__ == "__main__":
    sys.exit(main())
