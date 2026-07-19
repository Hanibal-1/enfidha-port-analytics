import sqlite3


DB = "data/warehouse/enfidha_port.db"


SQL = """

DROP TABLE IF EXISTS agg_location_risk;


CREATE TABLE agg_location_risk AS


WITH hydro AS (

    SELECT

        location_id,

        AVG(flood_risk_index) AS average_flood_risk,

        MAX(flood_risk_index) AS maximum_flood_risk


    FROM fact_hydrology_daily

    GROUP BY location_id

),


sediment AS (

    SELECT

        location_id,

        AVG(sediment_risk_index) AS average_sediment_risk,

        SUM(sediment_load_tons) AS total_sediment_load


    FROM fact_sediment_daily

    GROUP BY location_id

)


SELECT

    l.location_id,

    l.latitude,

    l.longitude,

    l.elevation_m,

    l.slope_degree,

    l.zone,

    l.watershed_id,


    ROUND(
        h.average_flood_risk,
        2
    ) AS average_flood_risk,


    ROUND(
        h.maximum_flood_risk,
        2
    ) AS maximum_flood_risk,


    ROUND(
        s.average_sediment_risk,
        2
    ) AS average_sediment_risk,


    ROUND(
        s.total_sediment_load,
        2
    ) AS total_sediment_load,


    CASE

        WHEN h.maximum_flood_risk < 25
            THEN 'Low'

        WHEN h.maximum_flood_risk < 50
            THEN 'Moderate'

        WHEN h.maximum_flood_risk < 75
            THEN 'High'

        ELSE 'Critical'

    END AS flood_risk_level,


    CASE

        WHEN s.average_sediment_risk < 25
            THEN 'Low'

        WHEN s.average_sediment_risk < 50
            THEN 'Moderate'

        WHEN s.average_sediment_risk < 75
            THEN 'High'

        ELSE 'Critical'

    END AS sediment_risk_level



FROM dim_location l


JOIN hydro h

ON l.location_id = h.location_id


JOIN sediment s

ON l.location_id = s.location_id;

"""


if __name__ == "__main__":


    print("=" * 60)
    print("CREATING ANALYTICS TABLES")
    print("=" * 60)


    conn = sqlite3.connect(DB)


    try:

        print("Building agg_location_risk ...")


        conn.executescript(SQL)


        print(
            "agg_location_risk created successfully"
        )


        result = conn.execute(
            """
            SELECT COUNT(*)
            FROM agg_location_risk
            """
        )


        count = result.fetchone()[0]


        print(
            f"Rows created: {count}"
        )


    except Exception as e:

        print("ERROR:")
        print(e)

        raise


    finally:

        conn.close()


        print(
            "Database connection closed"
        )