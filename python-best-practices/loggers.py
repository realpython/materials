# Avoid this:
# import logging

# logging.basicConfig(level=logging.INFO)

# def authenticate_user(username: str, password: str) -> bool:
#     if username != "admin" or password != "secret":
#         logging.error("Authentication failed for user %s", username)
#         return False

#     logging.info("User %s authenticated successfully", username)
#     return True


# Favor this:
import logging

log = logging.getLogger(__name__)


def authenticate_user(username: str, password: str) -> bool:
    if username != "admin" or password != "secret":
        log.error("Authentication failed for user %s", username)
        return False

    log.info("User %s authenticated successfully", username)
    return True
