# This file will establish the actual connection to PostgreSQL

from sqlalchemy import create_engine, text
from src.utils.config import DATABASE_URL

# Create database engine
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

# Test database connection
def test_connection():

    try:
        with engine.connect() as connection:

            result = connection.execute(
                text("SELECT version()")
            )

            print("Database connected successfully!")

            print(result.scalar())

            return True

    except Exception as e:

        print("Database connection failed!")

        print(e)

        return False