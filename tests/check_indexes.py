import sqlite3
import pandas as pd


DB = "data/warehouse/enfidha_port.db"


conn = sqlite3.connect(DB)


indexes = pd.read_sql(
    """
    SELECT 
        name,
        tbl_name
    FROM sqlite_master
    WHERE type='index'
    """,
    conn
)


print("="*60)
print("WAREHOUSE INDEXES")
print("="*60)


print(indexes)


conn.close()