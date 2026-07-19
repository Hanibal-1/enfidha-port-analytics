import sqlite3
from pathlib import Path

DATABASE = Path("database/enfidha_port.db")
SCHEMA = Path("sql/schema.sql")


def create_database():

    DATABASE.parent.mkdir(exist_ok=True)

    conn = sqlite3.connect(DATABASE)

    with open(SCHEMA, "r", encoding="utf-8") as f:
        conn.executescript(f.read())

    conn.commit()
    conn.close()

    print("=" * 50)
    print("Database created successfully")
    print("=" * 50)


if __name__ == "__main__":
    create_database()