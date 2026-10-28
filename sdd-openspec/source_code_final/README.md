# habits

A tiny command-line habit tracker.

```console
$ habits add read
$ habits done read
$ habits done read --yesterday
$ habits done read --date 2026-10-08
$ habits list
$ habits stats
```

`--date YYYY-MM-DD` backfills a check-in for any day up to 7 days back.

Check-ins are stored in `~/.habits.json`. Set `HABITS_FILE` to use a different file.
