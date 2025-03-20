# logger.py
import logging
import os
from datetime import datetime

def setup_logger(name, log_file="tmdb_api.log", level=logging.INFO):
    """Set up a logger with output to file and console."""
    # Log format: timestamp, level, message
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Create logs directory if it doesn't exist
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Path to log file
    log_path = os.path.join(log_dir, log_file)

    # File handler
    file_handler = logging.FileHandler(log_path)
    file_handler.setFormatter(formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Configure logger
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

if __name__ == "__main__":
    logger = setup_logger("example")
    logger.info("Logger initialized")
    logger.error("This is an example error")