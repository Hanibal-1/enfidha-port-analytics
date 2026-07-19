import sqlite3
import pandas as pd
import os


DB = "data/warehouse/enfidha_port.db"


def load_table(df, table_name, conn):

    print(f"\nLoading table: {table_name}")
    print(f"Rows: {len(df)}")

    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False
    )

    print(f"{table_name} loaded successfully")


def check_file(path):

    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Missing file: {path}"
        )


if __name__ == "__main__":

    print("=" * 60)
    print("ENFIDHA PORT WAREHOUSE LOADER")
    print("=" * 60)


    print("\nConnecting database...")

    conn = sqlite3.connect(DB)


    try:

        # =========================
        # DIMENSIONS
        # =========================

        print("\n--- Loading Dimensions ---")


        check_file(
            "data/processed/spatial_locations.csv"
        )

        load_table(
            pd.read_csv(
                "data/processed/spatial_locations.csv"
            ),
            "dim_location",
            conn
        )


        check_file(
            "data/raw/soil.csv"
        )

        load_table(
            pd.read_csv(
                "data/raw/soil.csv"
            ),
            "dim_soil",
            conn
        )


        check_file(
            "data/raw/landcover.csv"
        )

        load_table(
            pd.read_csv(
                "data/raw/landcover.csv"
            ),
            "dim_landcover",
            conn
        )


        check_file(
            "data/raw/watersheds.csv"
        )

        load_table(
            pd.read_csv(
                "data/raw/watersheds.csv"
            ),
            "dim_watershed",
            conn
        )


        # =========================
        # FACT WEATHER
        # =========================

        print("\n--- Loading Weather Fact ---")


        check_file(
            "data/raw/weather_daily.parquet"
        )


        weather = pd.read_parquet(
            "data/raw/weather_daily.parquet"
        )


        load_table(
            weather,
            "fact_weather_daily",
            conn
        )


        # =========================
        # FACT HYDROLOGY
        # =========================

        print("\n--- Loading Hydrology Fact ---")


        check_file(
            "data/processed/hydrology_daily.parquet"
        )


        hydro = pd.read_parquet(
            "data/processed/hydrology_daily.parquet"
        )


        load_table(
            hydro[
                [
                    "date",
                    "location_id",
                    "runoff_mm",
                    "runoff_volume_m3",
                    "flood_risk_index"
                ]
            ],
            "fact_hydrology_daily",
            conn
        )


        # =========================
        # FACT SEDIMENT
        # =========================

        print("\n--- Loading Sediment Fact ---")


        check_file(
            "data/processed/sediment_risk_daily.parquet"
        )


        sediment = pd.read_parquet(
            "data/processed/sediment_risk_daily.parquet"
        )


        load_table(
            sediment[
                [
                    "date",
                    "location_id",
                    "sediment_load_tons",
                    "sediment_risk_index"
                ]
            ],
            "fact_sediment_daily",
            conn
        )


        # =========================
        # FACT RISK
        # =========================

        print("\n--- Loading Risk Assessment Fact ---")


        check_file(
            "data/processed/risk_assessment_daily.parquet"
        )


        risk = pd.read_parquet(
            "data/processed/risk_assessment_daily.parquet"
        )


        load_table(
            risk[
                [
                    "date",
                    "location_id",
                    "flood_risk_level",
                    "sediment_risk_level"
                ]
            ],
            "fact_risk_assessment",
            conn
        )


        print("\n" + "=" * 60)
        print("WAREHOUSE LOADING COMPLETED")
        print("=" * 60)


    except Exception as e:

        print("\nERROR DURING LOADING")
        print(e)

        raise


    finally:

        conn.close()

        print("\nDatabase connection closed")