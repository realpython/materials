import sys

from loguru import logger

logger.remove()
logger.add(sys.stderr, serialize=True)
logger.info("User logged in", user_id=123)
