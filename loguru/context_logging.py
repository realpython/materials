import sys

from loguru import logger

logger.remove()
logger.add(sys.stderr, format="{time} | {level} | {message} | {extra}")

user_logger = logger.bind(user_id=123)
user_logger.info("User logged in")
user_logger.info("User started a session")

with logger.contextualize(request_id="abc789"):
    logger.info("Processing request")
    logger.info("Request completed")

logger.info("Request is processed, this will not show extra context")
