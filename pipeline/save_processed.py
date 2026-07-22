from pathlib import Path

from logger import logger


def save_processed_data(df):

    BASE_DIR = Path(__file__).resolve().parent.parent

    file = BASE_DIR / "data" / "processed" / "clean_sales.csv"

    df.to_csv(file, index=False)

    logger.info(f"Saved processed data: {file}")