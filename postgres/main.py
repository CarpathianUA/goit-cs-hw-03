from sqlalchemy import create_engine, text

from db_schema.create_db import create_database
from db_schema.seed import seed_db
from models.base import Base

from constants.database import SQLALCHEMY_DATABASE_URL, QUERIES_FILE_PATH

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
queries_file_path = QUERIES_FILE_PATH


if __name__ == "__main__":
    with open(queries_file_path, "r") as file:
        sql_commands = file.read().split(";")
    with engine.connect() as conn:
        create_database(conn)
        Base.metadata.create_all(conn)  # create tables from Base metadata
        seed_db(conn)  # seed database
        for command in sql_commands:
            if command.strip():
                try:
                    result = conn.execute(text(command))
                    if result.returns_rows:
                        for row in result:
                            print(row)
                except Exception as e:
                    print(f"Error executing query: {e}")

        conn.commit()
