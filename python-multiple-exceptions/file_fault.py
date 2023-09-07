# file_fault.py

from os import strerror

try:
    with open("datafile.txt", mode="rt") as f:
        print(f.readlines())
except OSError as error:
    print(strerror(error.errno))
