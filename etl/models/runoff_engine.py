import pandas as pd
import numpy as np



CELL_AREA_M2 = 48000



def calculate_flood_risk(row):


    # Rainfall component

    rainfall_score = min(
        row.rainfall_mm / 100 * 40,
        40
    )


    # Low elevation increases risk

    elevation_score = max(
        0,
        (20 - row.elevation_m) / 20 * 25
    )


    # Flat areas accumulate water

    slope_score = max(
        0,
        (10 - row.slope_degree) / 10 * 15
    )


    # Land cover effect

    landcover_score = (
        row.landcover_factor
        * 20
    )


    risk = (
        rainfall_score
        +
        elevation_score
        +
        slope_score
        +
        landcover_score
    )


    return round(
        min(risk,100),
        2
    )



def generate_hydrology():


    weather = pd.read_parquet(
        "data/raw/weather_daily.parquet"
    )


    locations = pd.read_csv(
        "data/processed/spatial_locations.csv"
    )


    soils = pd.read_csv(
        "data/raw/soil.csv"
    )


    landcover = pd.read_csv(
        "data/raw/landcover.csv"
    )


    # Merge GIS attributes

    df = weather.merge(
        locations,
        on="location_id"
    )


    df = df.merge(
        soils[
            [
                "soil_id",
                "runoff_coefficient"
            ]
        ],
        on="soil_id"
    )


    df = df.merge(
        landcover[
            [
                "landcover_id",
                "runoff_factor"
            ]
        ],
        on="landcover_id"
    )


    df["runoff_coefficient_final"] = (
        df.runoff_coefficient
        *
        df.runoff_factor
    )


    df["runoff_mm"] = (
        df.rainfall_mm
        *
        df.runoff_coefficient_final
    )


    df["runoff_volume_m3"] = (
        df.runoff_mm / 1000
        *
        CELL_AREA_M2
    )


    df["landcover_factor"] = (
        df.runoff_factor
    )


    df["flood_risk_index"] = (
        df.apply(
            calculate_flood_risk,
            axis=1
        )
    )


    return df



if __name__ == "__main__":


    df = generate_hydrology()


    print("="*60)
    print("HYDROLOGY MODEL GENERATED")
    print("="*60)


    print(df.head())


    print("\nFlood risk statistics")

    print(
        df.flood_risk_index.describe()
    )


    df.to_parquet(
        "data/processed/hydrology_daily.parquet",
        index=False
    )


    print()

    print(
        f"Generated {len(df)} hydrology records"
    )