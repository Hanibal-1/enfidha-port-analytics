import pandas as pd


df = pd.read_parquet(
    "data/raw/weather_daily.parquet"
)


print("="*60)
print("WEATHER DATA VALIDATION")
print("="*60)


print("\nRows:")
print(len(df))


print("\nDate range:")

print(
    df.date.min(),
    "to",
    df.date.max()
)


print("\nMissing values:")

print(
    df.isna().sum()
)


print("\nRainfall statistics")

print(
    df.rainfall_mm.describe()
)


print("\nTemperature statistics")

print(
    df.temperature_c.describe()
)


print("\nExtreme rainfall days")

print(
    df[
        df.rainfall_mm > 50
    ].head()
)