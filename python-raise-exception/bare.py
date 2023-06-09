import logging

try:
    result = 42 / 0
except Exception as error:
    logging.error(error)
    raise error
