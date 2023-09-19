import timeit


def time_test(statement, globals, number):
    print(
        f"Timing {statement}",
        end=f"{30 * ' '}\r",  # Clear previous characters and reset cursor
    )
    return timeit.timeit(statement, globals=globals, number=number)


def print_results(times, name):
    print(f"\nRESULTS {name.upper()}:\n")
    print(
        "\n".join(
            [time[0] for time in sorted(times, key=lambda item: item[1])]
        ),
        end="\n\n",
    )


def timeit_multiple(
    tests: list[tuple[str, str]], *, name, globals, number=100
):
    times = []

    for test in tests:
        time = time_test(test[1], globals=globals, number=number)
        times.append((f"{test[0]:15}: {time:.3f} seconds", time))

    print("Done!", end=f"{30 * ' '}\n")

    print_results(times, name)
