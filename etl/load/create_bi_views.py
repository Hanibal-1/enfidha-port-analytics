import sqlite3


DB = "data/warehouse/enfidha_port.db"


SQL = """

-- =====================================================
-- 1. FLOOD RISK MAP VIEW
-- =====================================================

DROP VIEW IF EXISTS vw_flood_risk_map;


CREATE VIEW vw_flood_risk_map AS


SELECT

    location_id,

    latitude,

    longitude,

    zone,

    watershed_id,

    average_flood_risk,

    maximum_flood_risk,

    flood_risk_level


FROM agg_location_risk;




-- =====================================================
-- 2. SEDIMENT RISK MAP VIEW
-- =====================================================

DROP VIEW IF EXISTS vw_sediment_risk_map;


CREATE VIEW vw_sediment_risk_map AS


SELECT

    location_id,

    latitude,

    longitude,

    zone,

    watershed_id,

    total_sediment_load,

    average_sediment_risk,

    sediment_risk_level


FROM agg_location_risk;




-- =====================================================
-- 3. PORT SUMMARY KPI VIEW
-- =====================================================

DROP VIEW IF EXISTS vw_port_summary;


CREATE VIEW vw_port_summary AS


SELECT

    zone,


    ROUND(
        AVG(average_flood_risk),
        2
    ) AS avg_flood_risk,


    ROUND(
        AVG(average_sediment_risk),
        2
    ) AS avg_sediment_risk,


    ROUND(
        AVG(
            (
                average_flood_risk
                +
                average_sediment_risk
            ) / 2
        ),
        2
    ) AS vulnerability_score,


    COUNT(*) AS locations


FROM agg_location_risk


WHERE zone = 'Port'


GROUP BY zone;




-- =====================================================
-- 4. ZONE PERFORMANCE VIEW
-- =====================================================

DROP VIEW IF EXISTS vw_zone_analysis;


CREATE VIEW vw_zone_analysis AS


SELECT


    zone,


    COUNT(*) AS locations,


    ROUND(
        AVG(average_flood_risk),
        2
    ) AS avg_flood_risk,


    ROUND(
        AVG(average_sediment_risk),
        2
    ) AS avg_sediment_risk,


    ROUND(
        AVG(total_sediment_load),
        2
    ) AS avg_sediment_load



FROM agg_location_risk


GROUP BY zone;

"""



if __name__ == "__main__":


    print("=" * 60)
    print("CREATING BI VIEWS")
    print("=" * 60)


    conn = sqlite3.connect(DB)


    try:

        conn.executescript(SQL)


        print(
            "BI views created successfully"
        )


        views = conn.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type='view'
            """
        ).fetchall()


        print("\nCreated views:")

        for view in views:

            print(
                "-",
                view[0]
            )


    except Exception as e:

        print("ERROR:")
        print(e)

        raise


    finally:

        conn.close()

        print(
            "\nDatabase connection closed"
        )