import pandas as pd
import numpy as np


np.random.seed(42)



def assign_watershed(row):

    zone = row["zone"]
    lon = row["longitude"]
    lat = row["latitude"]


    # Port area

    if zone == "Port":

        return np.random.choice(
            [2,6],
            p=[0.7,0.3]
        )


    # Wetlands

    if zone == "Wetland":

        return 5


    # Coastal areas

    if zone == "Coastal":

        return np.random.choice(
            [1,5],
            p=[0.6,0.4]
        )


    # Hills

    if zone == "Hills":

        return 4


    # Agriculture

    if zone == "Agriculture":

        if lon < 10.410:

            return 3

        else:

            return 2


    return 2



def assign_watersheds():


    df = pd.read_csv(
        "data/processed/enriched_locations.csv"
    )


    df["watershed_id"] = (
        df.apply(
            assign_watershed,
            axis=1
        )
    )


    return df



if __name__ == "__main__":


    df = assign_watersheds()


    print("="*60)
    print("WATERSHED ASSIGNMENT COMPLETED")
    print("="*60)


    print(df.head())


    print("\nWatershed distribution")

    print(
        df.watershed_id.value_counts()
    )


    df.to_csv(
        "data/processed/spatial_locations.csv",
        index=False
    )


    print()

    print(
        f"Processed {len(df)} locations"
    )