import argparse
import os
import sys
from datetime import date

from habits import storage


def main(argv=None):
    parser = argparse.ArgumentParser(prog="habits")
    commands = parser.add_subparsers(dest="command", required=True)

    add = commands.add_parser("add", help="start tracking a new habit")
    add.add_argument("name")

    done = commands.add_parser("done", help="check in a habit")
    done.add_argument("name")
    done.add_argument("--yesterday", action="store_true")

    commands.add_parser("list", help="show all habits and their streaks")

    args = parser.parse_args(argv)
    path = os.environ.get("HABITS_FILE", storage.DEFAULT_PATH)
    tracker = storage.load(path)

    try:
        if args.command == "add":
            tracker.add(args.name)
            print(f"Tracking '{args.name}'.")
        elif args.command == "done":
            day = date.fromordinal(date.today().toordinal() - args.yesterday)
            tracker.check_in(args.name, day)
            print(
                f"Checked in '{args.name}'. Streak: {tracker.streak(args.name)}"
            )
        elif args.command == "list":
            for habit in tracker.habits.values():
                print(
                    f"{habit.name:<20} {tracker.streak(habit.name):>3} day(s)"
                )
    except (KeyError, ValueError) as error:
        print(f"Error: {error.args[0]}", file=sys.stderr)
        return 1

    storage.save(tracker, path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
