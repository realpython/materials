import functools

from data_repo import read as _read

data = functools.partial(_read.data, package=__package__)
path = functools.partial(_read.path, package=__package__)
