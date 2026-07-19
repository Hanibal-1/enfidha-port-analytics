import sqlite3
import pandas as pd


DB = "data/warehouse/enfidha_port.db"


conn = sqlite3.connect(DB)


tables = pd.read_sql(
    """
    SELECT name
    FROM sqlite_master
    WHERE type='table'
    """,
    conn
)


print("="*60)
print("WAREHOUSE TABLES")
print("="*60)

print(tables)


print("\nROW COUNTS")


for table in tables["name"]:

    count = pd.read_sql(
        f"SELECT COUNT(*) as cnt FROM {table}",
        conn
    )

    print(
        table,
        ":",
        count.iloc[0]["cnt"]
    )


conn.close()