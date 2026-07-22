import os
from dotenv import load_dotenv
from sqlalchemy import create_engine


# Ngarkon variablat nga .env
load_dotenv()


# Marrim të dhënat e databazës nga .env
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


# Krijojmë lidhjen me MySQL
connection_string = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


engine = create_engine(connection_string)


def get_connection():
    """
    Returns database engine connection
    """
    return engine


# Test connection
if __name__ == "__main__":

    try:
        connection = get_connection().connect()

        print("Database connection successful!")

        connection.close()

    except Exception as e:
        print("Database connection failed:")
        print(e)