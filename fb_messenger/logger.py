import logging


logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


def get_logger(name):
    """
    Get a logger for the given name, and set the level to match
    that of the LOGGINGLEVEL env var.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    return logger
