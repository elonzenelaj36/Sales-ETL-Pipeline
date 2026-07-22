import pandas as pd

from logger import logger


def transform_data(df):
    """
    Cleans and transforms sales data.
    """

    logger.info("Starting data transformation")

    initial_rows = len(df)

    # 1. Pastrojmë emrat e klientëve
    df["customer"] = df["customer"].str.strip().str.title()

    # 2. Rregullojmë datat në një format të vetëm
    df["order_date"] = pd.to_datetime(
        df["order_date"],
        errors="coerce"
    )

    # 3. Heqim rreshtat ku mungon data
    df = df.dropna(subset=["order_date"])

    # 4. Heqim porositë e dyfishta
    df = df.drop_duplicates(
        subset=["order_id"]
    )

    # 5. Krijojmë kolonën total
    df["total"] = df["quantity"] * df["price"]

    final_rows = len(df)

    logger.info(f"Rows before transformation: {initial_rows}")
    logger.info(f"Rows after transformation: {final_rows}")
    logger.info(f"Removed {initial_rows - final_rows} invalid/duplicate rows")

    return df