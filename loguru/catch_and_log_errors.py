from loguru import logger


@logger.catch
def divide(a, b):
    return a / b


divide(10, 0)
