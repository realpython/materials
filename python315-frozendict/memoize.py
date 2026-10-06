"""Cache a function that takes a mapping argument.

A plain dict is unhashable, so @cache rejects it. A frozendict hashes, so the
same call signature becomes cacheable.

Run with Python 3.15 or later:

    python memoize.py
"""

from functools import cache


@cache
def render_report(options):
    print(f"computing report for {options}")
    return f"<report {sorted(options.items())}>"


def main():
    settings = frozendict(theme="dark", rows=50)

    print("First call, nothing cached yet:")
    render_report(settings)

    print("Second call with an equal frozendict:")
    render_report(frozendict(rows=50, theme="dark"))

    print(f"Cache statistics: {render_report.cache_info()}")

    print("The same call with a plain dict:")
    try:
        render_report({"theme": "dark", "rows": 50})
    except TypeError as error:
        print(f"  TypeError: {error}")


if __name__ == "__main__":
    main()
