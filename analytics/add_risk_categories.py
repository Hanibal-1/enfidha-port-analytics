import pandas as pd



def classify_risk(value):

    if value < 25:
        return "Low"

    elif value < 50:
        return "Moderate"

    elif value < 75:
        return "High"

    else:
        return "Critical"



def generate_risk_assessment():


    hydro = pd.read_parquet(
        "data/processed/hydrology_daily.parquet"
    )


    sediment = pd.read_parquet(
        "data/processed/sediment_risk_daily.parquet"
    )


    df = hydro[
        [
            "date",
            "location_id",
            "zone",
            "watershed_id",
            "flood_risk_index"
        ]
    ].merge(

        sediment[
            [
                "date",
                "location_id",
                "sediment_risk_index",
                "sediment_load_tons"
            ]
        ],

        on=[
            "date",
            "location_id"
        ],

        how="left"

    )


    df["flood_risk_level"] = (
        df["flood_risk_index"]
        .apply(classify_risk)
    )


    df["sediment_risk_level"] = (
        df["sediment_risk_index"]
        .apply(classify_risk)
    )


    return df



if __name__ == "__main__":


    df = generate_risk_assessment()


    print("="*60)
    print("RISK ASSESSMENT GENERATED")
    print("="*60)


    print(df.head())


    print("\nFlood Risk Distribution")

    print(
        df.flood_risk_level.value_counts()
    )


    print("\nSediment Risk Distribution")

    print(
        df.sediment_risk_level.value_counts()
    )


    df.to_parquet(
        "data/processed/risk_assessment_daily.parquet",
        index=False
    )


    print()

    print(
        f"Generated {len(df)} risk records"
    )