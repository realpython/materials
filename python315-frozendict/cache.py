from functools import cache


@cache
def render_report(options):
    print(f"computing report for {options}")
    return f"<report {sorted(options.items())}>"


print(render_report(frozendict(theme="dark", rows=50)))
print(render_report(frozendict(rows=50, theme="dark")))
print(render_report.cache_info())
