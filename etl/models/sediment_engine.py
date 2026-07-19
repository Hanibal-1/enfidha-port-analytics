import pandas as pd
import numpy as np


CELL_AREA_M2 = 48000


def calculate_sediment_risk(row):


    # Rainfall impact
    rainfall_factor = min(
        row.rainfall_mm / 100,
        1
    )


    # Soil erosion potential
    soil_factor = row.erosion_factor


    # Slope influence

    slope_factor = min(
        row.slope_degree / 25,
        1
    )


    # Runoff influence

    runoff_factor = min(
        row.runoff_mm / 50,
        1
    )


    risk = (

        rainfall_factor * 30

        +

        soil_factor * 30

        +

        slope_factor * 25

        +

        runoff_factor * 15

    )


    return round(
        min(risk,100),
        2
    )



def generate_sediment_model():


    hydro = pd.read_parquet(
        "data/processed/hydrology_daily.parquet"
    )


    soils = pd.read_csv(
        "data/raw/soil.csv"
    )


    df = hydro.merge(
        soils[
            [
                "soil_id",
                "erosion_factor"
            ]
        ],
        on="soil_id"
    )


    df["sediment_risk_index"] = (
        df.apply(
            calculate_sediment_risk,
            axis=1
        )
    )


    # Approximate sediment load

    df["sediment_load_tons"] = (

        df.runoff_volume_m3

        *

        df.erosion_factor

        *

        0.001

    )


    return df



if __name__ == "__main__":


    df = generate_sediment_model()


    print("="*60)
    print("SEDIMENT MODEL GENERATED")
    print("="*60)


    print(df.head())


    print("\nSediment risk statistics")

    print(
        df.sediment_risk_index.describe()
    )


    print("\nSediment load statistics")

    print(
        df.sediment_load_tons.describe()
    )


    df.to_parquet(
        "data/processed/sediment_risk_daily.parquet",
        index=False
    )


    print()

    print(
        f"Generated {len(df)} sediment records"
    )