import sqlite3
import pandas as pd
import os


DB = "data/warehouse/enfidha_port.db"

EXPORT_DIR = "data/exports/powerbi"


TABLES = {

    "Executive_KPI": "vw_port_summary",

    "Flood_Risk_Map": "vw_flood_risk_map",

    "Sediment_Risk_Map": "vw_sediment_risk_map",

    "Zone_Analysis": "vw_zone_analysis",

    "Location_Risk": "agg_location_risk",

    "Risk_Threshold": "dim_risk_threshold",

    "Weather_Monthly": "vw_weather_monthly",

    "Hydrology_Monthly": "vw_hydrology_monthly"


}


def format_numeric_columns(df):
    """
    Round numeric columns to improve CSV readability.
    """

    numeric_columns = df.select_dtypes(include=["float64", "float32"]).columns

    df[numeric_columns] = df[numeric_columns].round(2)

    return df


def export_table(conn, file_name, table_name):

    print(f"Exporting {table_name}...")

    df = pd.read_sql(
        f"SELECT * FROM {table_name}",
        conn
    )

    df = format_numeric_columns(df)

    path = os.path.join(
        EXPORT_DIR,
        f"{file_name}.csv"
    )

    df.to_csv(
        path,
        index=False,
        encoding="utf-8-sig",
        float_format="%.2f"
    )

    print(
        f"   ✓ {file_name}.csv ({len(df):,} rows)"
    )


def main():

    print("=" * 60)
    print("ENFIDHA PORT - POWER BI EXPORT")
    print("=" * 60)

    os.makedirs(
        EXPORT_DIR,
        exist_ok=True
    )

    conn = sqlite3.connect(DB)

    try:

        for file_name, table_name in TABLES.items():

            export_table(
                conn,
                file_name,
                table_name
            )

    finally:

        conn.close()

    print()
    print("=" * 60)
    print("Export completed successfully.")
    print(f"Files exported to: {EXPORT_DIR}")
    print("=" * 60)


if __name__ == "__main__":

    main()