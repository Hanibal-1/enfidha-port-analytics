import sqlite3

conn = sqlite3.connect("data/warehouse/enfidha_port.db")

cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM agg_location_risk")
print("agg_location_risk:", cursor.fetchone()[0])

conn.close()


#import pandas as pd

#df = pd.read_csv("data/exports/powerbi/Location_Risk.csv")

#print(df.shape)
#print(df["average_flood_risk"].mean())