import sys

from loguru import logger

logger.remove()
logger.add(
    sys.stderr, format="{time} | {level} | {message} | {extra}", level="TRACE"
)


@logger.catch
def perform_action(user, action):
    with logger.contextualize(user=user, action=action):
        logger.trace("Starting action")
        logger.info("Performing action")
        if action not in ["login", "logout"]:
            logger.trace("Invalid action detected")
            raise ValueError("Invalid action")
        logger.success("Action completed")


perform_action("alice", "delete")
