import sqlite3
import pandas as pd

conn = sqlite3.connect("data/warehouse/enfidha_port.db")

df = pd.read_sql("""

SELECT

MIN(average_flood_risk) AS min_flood,
MAX(average_flood_risk) AS max_flood,
AVG(average_flood_risk) AS avg_flood,

MIN(average_sediment_risk) AS min_sed,
MAX(average_sediment_risk) AS max_sed,
AVG(average_sediment_risk) AS avg_sed

FROM agg_location_risk

""", conn)

print(df)

conn.close()