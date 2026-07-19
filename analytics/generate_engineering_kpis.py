import pandas as pd



def generate_kpis():

    hydro = pd.read_parquet(
        "data/processed/hydrology_daily.parquet"
    )


    sediment = pd.read_parquet(
        "data/processed/sediment_risk_daily.parquet"
    )


    locations = pd.read_csv(
        "data/processed/spatial_locations.csv"
    )


    df = hydro.copy()


    sed = sediment[
        [
            "date",
            "location_id",
            "sediment_risk_index",
            "sediment_load_tons"
        ]
    ]

    df = df.merge(
        sed,
        on=[
            "location_id",
            "date"
        ],
        how="left"
    )


    kpis = {

        "total_locations":
            df.location_id.nunique(),


        "average_flood_risk":
            round(
                df.flood_risk_index.mean(),
                2
            ),


        "maximum_flood_risk":
            round(
                df.flood_risk_index.max(),
                2
            ),


        "high_flood_risk_percentage":
            round(
                (
                    df.flood_risk_index > 70
                ).mean()
                *
                100,
                2
            ),


        "average_sediment_risk":
            round(
                df.sediment_risk_index.mean(),
                2
            ),


        "total_sediment_load_tons":
            round(
                df.sediment_load_tons.sum(),
                2
            ),


        "maximum_sediment_risk":
            round(
                df.sediment_risk_index.max(),
                2
            )

    }


    # Port specific analysis

    port = df[
        df.zone == "Port"
    ]


    kpis.update({

        "port_average_flood_risk":
            round(
                port.flood_risk_index.mean(),
                2
            ),


        "port_max_flood_risk":
            round(
                port.flood_risk_index.max(),
                2
            ),


        "port_average_sediment_risk":
            round(
                port.sediment_risk_index.mean(),
                2
            )

    })


    return pd.DataFrame(
        [
            kpis
        ]
    )



if __name__ == "__main__":


    df = generate_kpis()


    print("="*60)
    print("ENGINEERING KPI REPORT")
    print("="*60)


    print(df.T)


    df.to_parquet(
        "data/processed/engineering_kpis.parquet",
        index=False
    )