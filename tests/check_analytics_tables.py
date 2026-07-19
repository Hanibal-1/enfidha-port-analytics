import sqlite3
import pandas as pd


DB = "data/warehouse/enfidha_port.db"


conn = sqlite3.connect(DB)


df = pd.read_sql(
    """
    SELECT *
    FROM agg_location_risk
    LIMIT 10
    """,
    conn
)


print(df)


count = pd.read_sql(
    """
    SELECT COUNT(*) AS rows
    FROM agg_location_risk
    """,
    conn
)


print("\nTotal rows:")
print(count)


conn.close()