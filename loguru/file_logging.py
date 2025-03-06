from loguru import logger
import time
logger.add(sink="app.log", rotation="5 seconds", retention="1 minute")
for i in range(100):
   logger.info(f"Processing item #{i}")
   time.sleep(2)