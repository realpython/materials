from timeit import timeit

from test_cases import build_list

TIMES = 10_000
long_name_list = build_list(100_000, "Fake Python", "Real Python", 50_000)

gen_time = timeit(
    stmt="find_match_gen(long_name_list,'Real Python')",
    setup="from generator import find_match_gen",
    globals=globals(),
    number=TIMES,
)
loop_time = timeit(
    stmt="find_match_loop(long_name_list, 'Real Python')",
    setup="from looping import find_match_loop",
    globals=globals(),
    number=TIMES,
)

print(
    f"""\
{gen_time=:.4f} seconds
{loop_time=:.4f} seconds
"""
)
