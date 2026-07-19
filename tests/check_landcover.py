import pandas as pd


df = pd.read_csv(
    "data/raw/landcover.csv"
)


print("="*50)
print("LAND COVER VALIDATION")
print("="*50)


print(df)


print("\nMissing values:")
print(df.isna().sum())


print("\nStatistics:")
print(df.describe())