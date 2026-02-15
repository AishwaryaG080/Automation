import logging
import os
from datetime import datetime

def setup_logger():
    if not os.path.exists("Logs"):
        os.makedirs("Logs")

    log_file = f"Logs/backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return log_file

def log_info(msg):
    logging.info(msg)

def log_error(msg):
    logging.error(msg)