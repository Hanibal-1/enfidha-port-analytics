import pandas as pd


df = pd.read_csv(
    "data/raw/location_grid.csv"
)


port_lat = 36.0758
port_lon = 10.4386


df["distance"] = (
    (df.latitude - port_lat)**2
    +
    (df.longitude - port_lon)**2
)


nearest = df.sort_values(
    "distance"
).head(5)


print(nearest)