import pandas as pd


def generate_watersheds():

    watersheds = [

        {
            "watershed_id": 1,
            "watershed_name": "Northern Coastal Basin",
            "area_km2": 35,
            "stream_order": 2,
            "outlet_latitude": 36.120,
            "outlet_longitude": 10.500
        },

        {
            "watershed_id": 2,
            "watershed_name": "Central Enfidha Basin",
            "area_km2": 50,
            "stream_order": 3,
            "outlet_latitude": 36.0758,
            "outlet_longitude": 10.4386
        },

        {
            "watershed_id": 3,
            "watershed_name": "Southern Agricultural Basin",
            "area_km2": 60,
            "stream_order": 3,
            "outlet_latitude": 36.030,
            "outlet_longitude": 10.420
        },

        {
            "watershed_id": 4,
            "watershed_name": "Western Hills Basin",
            "area_km2": 80,
            "stream_order": 4,
            "outlet_latitude": 36.050,
            "outlet_longitude": 10.370
        },

        {
            "watershed_id": 5,
            "watershed_name": "Wetland Lagoon Basin",
            "area_km2": 25,
            "stream_order": 2,
            "outlet_latitude": 36.090,
            "outlet_longitude": 10.490
        },

        {
            "watershed_id": 6,
            "watershed_name": "Industrial Drainage Basin",
            "area_km2": 20,
            "stream_order": 2,
            "outlet_latitude": 36.070,
            "outlet_longitude": 10.460
        }

    ]

    return pd.DataFrame(watersheds)



if __name__ == "__main__":

    df = generate_watersheds()


    print("="*50)
    print("WATERSHED DIMENSION GENERATED")
    print("="*50)


    print(df)


    df.to_csv(
        "data/raw/watersheds.csv",
        index=False
    )


    print()

    print(
        f"Generated {len(df)} watersheds"
    )