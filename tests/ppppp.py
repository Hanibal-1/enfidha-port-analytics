import pandas as pd

df = pd.read_csv("data/exports/powerbi/Location_Risk.csv")

print(df.shape)
print(df["average_flood_risk"].head(10))
print(df["average_flood_risk"].mean())
print(df.dtypes)