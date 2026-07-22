from logger import logger


def validate_data(df):
    """
    Validates sales data and separates valid and rejected rows.
    """

    logger.info("Starting data validation")

    initial_rows = len(df)

    valid_df = df.copy()

    rejected_df = valid_df[
        (valid_df["quantity"] <= 0) |
        (valid_df["price"] <= 0) |
        (valid_df["order_id"].isna()) |
        (valid_df["order_date"].isna())
    ]

    valid_df = valid_df.drop(rejected_df.index)

    logger.info(f"Rows before validation: {initial_rows}")
    logger.info(f"Valid rows: {len(valid_df)}")
    logger.info(f"Rejected rows: {len(rejected_df)}")

    return valid_df, rejected_df