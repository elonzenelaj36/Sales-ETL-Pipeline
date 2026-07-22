from pathlib import Path

from logger import logger


def save_rejected_data(df):

    if len(df) == 0:
        logger.info("No rejected data found")
        return

    BASE_DIR = Path(__file__).resolve().parent.parent

    file = BASE_DIR / "data" / "rejected" / "rejected_sales.csv"

    df.to_csv(file, index=False)

    logger.info(f"Saved rejected data: {file}")