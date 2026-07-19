import pandas as pd


df = pd.read_csv(
    "data/raw/location_grid.csv"
)


print("="*50)
print("SPATIAL DATA VALIDATION")
print("="*50)


print("\nRows:")
print(len(df))


print("\nMissing values:")
print(df.isna().sum())


print("\nElevation:")
print(df.elevation_m.describe())


print("\nSlope:")
print(df.slope_degree.describe())


print("\nZones:")
print(df.zone.value_counts())


print("\nCoordinates:")
print(
    df[
        [
            "latitude",
            "longitude"
        ]
    ].describe()
)