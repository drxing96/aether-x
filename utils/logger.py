# utils/logger.py

import logging
import sys

def get_logger(name: str) -> logging.Logger:
    """
    Returns a logger with a standard output handler.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # You can adjust the log level as needed

    # Avoid adding multiple handlers if get_logger is called multiple times
    if not logger.handlers:
        console_handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
        )
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger