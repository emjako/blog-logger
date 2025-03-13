from config.logger import get_logger
from core.traitement import process
import pandas as pd

logger = get_logger(__name__)

def main():
    logger.info("Démarrage du programme")
    df = pd.read_csv("data/input.csv")
    process(df)

if __name__ == "__main__":
    main()
