from collections import namedtuple

from database import get_column_names

Passenger = namedtuple("Passenger", get_column_names("passenger"), rename=True)
