# catch_first_only.py

exceptions = [ZeroDivisionError(), FileNotFoundError(), NameError()]
num_zd_errors = num_fnf_errors = num_name_errors = 0

try:
    for e in exceptions:
        raise e
except ZeroDivisionError:
    num_zd_errors += 1
except FileNotFoundError:
    num_fnf_errors += 1
except NameError:
    num_name_errors += 1
finally:
    print(f"ZeroDivisionError was raised {num_zd_errors} times.")
    print(f"FileNotFoundError was raised {num_fnf_errors} times.")
    print(f"NameError was raised {num_name_errors} times.")
