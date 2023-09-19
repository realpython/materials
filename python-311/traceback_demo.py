# traceback_demo.py

import sys
import traceback


def tb_last(tb):
    frame, *_ = traceback.extract_tb(tb, limit=1)
    return f"{frame.name}:{frame.lineno}"


def bad_calculation():
    return 1 / 0


def main():
    try:
        bad_calculation()
    except ZeroDivisionError as err:
        err_tb = err.__traceback__
        err = err.with_traceback(err_tb.tb_next)

        _exc_type, exc_value, exc_tb = sys.exc_info()
        print(f"{tb_last(exc_value.__traceback__) = }")
        print(f"{tb_last(exc_tb)                  = }")


if __name__ == "__main__":
    main()
