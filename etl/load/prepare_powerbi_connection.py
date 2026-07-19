import sqlite3
import os
import pandas as pd


DB = "data/warehouse/enfidha_port.db"

EXPORT_DIR = "data/exports/powerbi"



def check_database():

    if not os.path.exists(DB):

        raise FileNotFoundError(
            f"Database not found: {DB}"
        )

    print("✓ SQLite database found")



def list_objects(conn):

    query = """

    SELECT 
        type,
        name

    FROM sqlite_master

    WHERE type IN ('table','view')

    ORDER BY type,name;

    """

    df = pd.read_sql(
        query,
        conn
    )

    print("\nDatabase objects:")
    print(df.to_string(index=False))



def export_powerbi_tables(conn):

    os.makedirs(
        EXPORT_DIR,
        exist_ok=True
    )


    objects = [

        "agg_location_risk",

        "vw_flood_risk_map",

        "vw_sediment_risk_map",

        "vw_port_summary",

        "vw_zone_analysis",

        "dim_watershed",

        "dim_risk_threshold"

    ]


    for table in objects:


        print(
            f"Exporting {table}..."
        )


        df = pd.read_sql(

            f"""
            SELECT *
            FROM {table}
            """,

            conn

        )


        path = os.path.join(

            EXPORT_DIR,

            f"{table}.csv"

        )


        df.to_csv(

            path,

            index=False

        )


        print(

            f"  {len(df)} rows exported"

        )



if __name__ == "__main__":


    print("="*60)

    print(
        "POWER BI CONNECTION PREPARATION"
    )

    print("="*60)



    check_database()



    conn = sqlite3.connect(DB)


    try:

        list_objects(conn)


        export_powerbi_tables(conn)



    finally:

        conn.close()


    print("\nDone.")