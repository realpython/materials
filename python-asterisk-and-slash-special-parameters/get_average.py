def get_average(*args):
    print(args)
    return sum(args) / len(args)


get_average(1, 2, 3)
get_average(1, 3, 5, 7, 9)
