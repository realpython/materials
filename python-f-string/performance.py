import timeit

name = "Linda Smith"
age = 40
strings = {
    "Modulo operator": "'Name: %s Age: %s' % (name, age)",
    ".format() method": "'Name: {} Age: {}'.format(name, age)",
    "f_string": "f'Name: {name} Age: {age}'",
}


def run_performance_test(strings):
    max_length = len(max(strings, key=len))
    for tool, string in strings.items():
        time = timeit.timeit(string, number=1000000, globals=globals()) * 1000
        print(f"{tool}: {time:>{max_length - len(tool) + 6}.2f} ms")


run_performance_test(strings)
