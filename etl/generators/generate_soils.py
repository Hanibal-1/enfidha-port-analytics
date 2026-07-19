import pandas as pd


def generate_soils():

    soils = [

        {
            "soil_id": 1,
            "soil_name": "Sand",
            "permeability": 0.90,
            "runoff_coefficient": 0.20,
            "erosion_factor": 0.40,
            "stability_factor": 0.65
        },

        {
            "soil_id": 2,
            "soil_name": "Sandy Loam",
            "permeability": 0.75,
            "runoff_coefficient": 0.35,
            "erosion_factor": 0.50,
            "stability_factor": 0.70
        },

        {
            "soil_id": 3,
            "soil_name": "Silt",
            "permeability": 0.45,
            "runoff_coefficient": 0.60,
            "erosion_factor": 0.70,
            "stability_factor": 0.55
        },

        {
            "soil_id": 4,
            "soil_name": "Clay",
            "permeability": 0.25,
            "runoff_coefficient": 0.80,
            "erosion_factor": 0.85,
            "stability_factor": 0.45
        },

        {
            "soil_id": 5,
            "soil_name": "Limestone",
            "permeability": 0.55,
            "runoff_coefficient": 0.50,
            "erosion_factor": 0.60,
            "stability_factor": 0.85
        }

    ]

    return pd.DataFrame(soils)



if __name__ == "__main__":


    df = generate_soils()


    print("="*50)
    print("SOIL DIMENSION GENERATED")
    print("="*50)

    print(df)


    df.to_csv(
        "data/raw/soil.csv",
        index=False
    )


    print()

    print(
        f"Generated {len(df)} soil types"
    )