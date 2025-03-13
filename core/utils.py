from config.logger import get_logger
logger = get_logger(__name__)

def addition(a, b):
    """
    Additionne deux nombres.

    Args:
        a (int | float): premier opérande
        b (int | float): second opérande

    Returns:
        int | float: résultat de l'addition
    """
    logger.debug(f"Addition de {a} + {b}")
    return a + b
