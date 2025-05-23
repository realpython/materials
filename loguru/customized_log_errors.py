from loguru import logger


@logger.catch(message="Database connection failed", level="ERROR")
def connect_to_db(host, port):
    if port < 1000:
        raise ValueError("Invalid port number")
    # Simulated database connection
    return 1 / 0  # Simulate error


connect_to_db("localhost", 123)
