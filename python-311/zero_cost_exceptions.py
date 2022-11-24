import dis


def inverse(number):
    try:
        return 1 / number
    except ZeroDivisionError:
        print("0 has no inverse")


dis.dis(inverse)
