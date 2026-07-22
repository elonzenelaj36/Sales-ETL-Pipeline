import pandas as pd

from logger import logger


def extract_data(file_path):
    """
    Reads data from a CSV file.
    """

    logger.info(f"Reading file: {file_path}")

    df = pd.read_csv(file_path)

    logger.info(f"Extracted {len(df)} rows")

    return df