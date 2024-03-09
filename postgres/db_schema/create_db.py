from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.exc import ProgrammingError


def create_database(engine, db_name="postgres"):
    try:
        result = engine.execute(
            text(f"SELECT 1 FROM pg_database WHERE datname='{db_name}'")
        )
        if not result.fetchone():
            engine.execute(text(f"CREATE DATABASE {db_name}"))
    except ProgrammingError as e:
        print(f"Error creating database: {e}")
