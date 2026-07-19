import pandas as pd


def generate_landcover():

    landcover = [

        {
            "landcover_id": 1,
            "landcover_name": "Port Infrastructure",
            "runoff_factor": 0.95,
            "infiltration_factor": 0.05,
            "roughness_factor": 0.10,
            "engineering_factor": 0.90
        },

        {
            "landcover_id": 2,
            "landcover_name": "Industrial",
            "runoff_factor": 0.85,
            "infiltration_factor": 0.15,
            "roughness_factor": 0.20,
            "engineering_factor": 0.75
        },

        {
            "landcover_id": 3,
            "landcover_name": "Urban",
            "runoff_factor": 0.75,
            "infiltration_factor": 0.25,
            "roughness_factor": 0.30,
            "engineering_factor": 0.70
        },

        {
            "landcover_id": 4,
            "landcover_name": "Agriculture",
            "runoff_factor": 0.45,
            "infiltration_factor": 0.65,
            "roughness_factor": 0.60,
            "engineering_factor": 0.55
        },

        {
            "landcover_id": 5,
            "landcover_name": "Wetland",
            "runoff_factor": 0.20,
            "infiltration_factor": 0.80,
            "roughness_factor": 0.90,
            "engineering_factor": 0.30
        },

        {
            "landcover_id": 6,
            "landcover_name": "Bare Soil",
            "runoff_factor": 0.60,
            "infiltration_factor": 0.40,
            "roughness_factor": 0.35,
            "engineering_factor": 0.45
        },

        {
            "landcover_id": 7,
            "landcover_name": "Water",
            "runoff_factor": 1.00,
            "infiltration_factor": 0.00,
            "roughness_factor": 0.05,
            "engineering_factor": 0.10
        }

    ]


    return pd.DataFrame(landcover)



if __name__ == "__main__":

    df = generate_landcover()


    print("="*50)
    print("LAND COVER DIMENSION GENERATED")
    print("="*50)

    print(df)


    df.to_csv(
        "data/raw/landcover.csv",
        index=False
    )


    print()

    print(
        f"Generated {len(df)} land cover classes"
    )