# GitHub CLI Examples

`open_bugs.py` lists the newest open issues labeled `bug` in a public
GitHub repository by calling `gh issue list --json` from Python.

## Run

Install [GitHub CLI](https://cli.github.com/), run `gh auth login`, and then:

```console
$ python open_bugs.py
$ python open_bugs.py realpython/reader
```

The script uses only the standard library and makes read-only calls.
