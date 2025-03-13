from config.logger import get_logger
logger = get_logger(__name__)

def addition(a, b):
    logger.debug(f"Addition de {a} + {b}")
    return a + b
