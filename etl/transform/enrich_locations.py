import pandas as pd
import numpy as np


np.random.seed(42)



def assign_soil(zone):

    if zone == "Coastal":
        return np.random.choice(
            [1,2],
            p=[0.6,0.4]
        )

    elif zone == "Wetland":
        return np.random.choice(
            [3,4],
            p=[0.7,0.3]
        )

    elif zone == "Agriculture":
        return np.random.choice(
            [2,3],
            p=[0.5,0.5]
        )

    elif zone == "Hills":
        return np.random.choice(
            [4,5],
            p=[0.4,0.6]
        )

    else:
        return 2



def assign_landcover(zone):

    if zone == "Port":
        return 1

    elif zone == "Wetland":
        return 5

    elif zone == "Agriculture":
        return 4

    elif zone == "Coastal":
        return np.random.choice(
            [6,7],
            p=[0.7,0.3]
        )

    elif zone == "Hills":
        return np.random.choice(
            [4,6],
            p=[0.4,0.6]
        )

    else:
        return 6



def enrich_locations():


    locations = pd.read_csv(
        "data/raw/location_grid.csv"
    )


    locations["soil_id"] = (
        locations["zone"]
        .apply(assign_soil)
    )


    locations["landcover_id"] = (
        locations["zone"]
        .apply(assign_landcover)
    )


    return locations



if __name__ == "__main__":


    df = enrich_locations()


    print("="*60)
    print("LOCATION ENRICHMENT COMPLETED")
    print("="*60)


    print(df.head())


    print("\nSoil distribution")

    print(
        df.soil_id.value_counts()
    )


    print("\nLand cover distribution")

    print(
        df.landcover_id.value_counts()
    )


    df.to_csv(
        "data/processed/enriched_locations.csv",
        index=False
    )


    print()

    print(
        f"Processed {len(df)} locations"
    )