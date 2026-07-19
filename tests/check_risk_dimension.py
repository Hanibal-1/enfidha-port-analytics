import sqlite3
import pandas as pd


DB = "data/warehouse/enfidha_port.db"


conn = sqlite3.connect(DB)


df = pd.read_sql(
    """
    SELECT *
    FROM dim_risk_threshold
    """,
    conn
)


print(df)


conn.close()