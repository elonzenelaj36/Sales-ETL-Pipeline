from logger import logger

from database.connection import get_connection
from sqlalchemy import text

from datetime import datetime


def load_data(df):
    """
    Loads transformed data into MySQL database
    """

    logger.info("Starting data loading")

    engine = get_connection()

    try:

        # Merr order_id ekzistuese nga databaza
        existing_orders = []

        with engine.connect() as connection:

            result = connection.execute(
                text("SELECT order_id FROM sales")
            )

            existing_orders = [
                row[0] for row in result
            ]


        # Mbajmë vetëm të dhënat e reja
        new_data = df[
            ~df["order_id"].isin(existing_orders)
        ].copy()


        if new_data.empty:

            logger.info("No new data to load")
            return


        # Shtojmë kohën kur u futën në databazë
        new_data["created_at"] = datetime.now()


        # Futim të dhënat në MySQL
        new_data.to_sql(
            name="sales",
            con=engine,
            if_exists="append",
            index=False
        )


        logger.info(
            f"Loaded {len(new_data)} rows into database"
        )

        logger.info(
            "Data loaded successfully!"
        )


    except Exception as e:

        logger.error(
            f"Loading failed: {e}"
        )

        raise