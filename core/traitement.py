from config.logger import get_logger
from core.utils import addition
logger = get_logger(__name__)

def process(df):
    """
    Traite un DataFrame : affiche des informations et effectue un calcul.

    Args:
        df (pd.DataFrame): jeu de données à traiter
    """
    logger.info(f"Traitement du DataFrame : {df.shape[0]} lignes")
    somme = addition(10, 5)
    logger.debug(f"Résultat de l'addition : {somme}")
