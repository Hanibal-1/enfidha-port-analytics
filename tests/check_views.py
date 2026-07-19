import sqlite3
import pandas as pd


DB = "data/warehouse/enfidha_port.db"


conn = sqlite3.connect(DB)


view = "vw_port_summary"


df = pd.read_sql(
    f"SELECT * FROM {view} LIMIT 5",
    conn
)


print(df)


conn.close()