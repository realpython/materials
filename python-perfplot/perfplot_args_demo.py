import time

import perfplot


def setup(n):
    print(f"setting up {n}")
    return n * "#"


def kernel_one(setup_result):
    print(f"kernel one: {setup_result}")
    time.sleep(1)
    return setup_result


def kernel_two(setup_result):
    print(f"kernel two: {setup_result}")
    time.sleep(1.5)
    return setup_result


perfplot.show(
    n_range=[1, 2, 3],
    setup=setup,
    kernels=[kernel_one, kernel_two],
    target_time_per_measurement=4,
)
