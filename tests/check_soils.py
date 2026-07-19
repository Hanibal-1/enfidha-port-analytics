import pandas as pd


df = pd.read_csv(
    "data/raw/soil.csv"
)


print("="*50)
print("SOIL VALIDATION")
print("="*50)


print(df)


print("\nMissing values:")
print(df.isna().sum())


print("\nValue ranges:")

print(
    df[
        [
            "permeability",
            "runoff_coefficient",
            "erosion_factor",
            "stability_factor"
        ]
    ].describe()
)