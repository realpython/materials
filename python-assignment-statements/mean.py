# def mean(sample):
#     n = len(sample)
#     if n == 0:
#         raise ValueError("input data required")
#     return sum(sample) / n


def mean(sample):
    if (n := len(sample)) == 0:
        raise ValueError("input data required")
    return sum(sample) / n
