import logging
from config.config import Config

def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(Config.LOG_LEVEL)

    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger

# Example of using the logger utility in scraper_service.py
# Single Responsibility Principle (SRP): `setup_logger` function is responsible for setting up logging configuration.
