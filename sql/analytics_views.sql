-- =====================================================
-- 1. FLOOD HOTSPOTS VIEW
-- =====================================================

DROP VIEW IF EXISTS vw_flood_hotspots;


CREATE VIEW vw_flood_hotspots AS

SELECT

    l.location_id,

    l.latitude,

    l.longitude,

    l.zone,

    l.watershed_id,

    ROUND(
        AVG(h.flood_risk_index),
        2
    ) AS average_flood_risk,


    ROUND(
        MAX(h.flood_risk_index),
        2
    ) AS maximum_flood_risk,


    CASE

        WHEN MAX(h.flood_risk_index) < 25
            THEN 'Low'

        WHEN MAX(h.flood_risk_index) < 50
            THEN 'Moderate'

        WHEN MAX(h.flood_risk_index) < 75
            THEN 'High'

        ELSE 'Critical'

    END AS risk_category


FROM fact_hydrology_daily h


JOIN dim_location l

ON h.location_id = l.location_id


GROUP BY

    l.location_id;





-- =====================================================
-- 2. SEDIMENT PRIORITY VIEW
-- =====================================================


DROP VIEW IF EXISTS vw_sediment_priority;


CREATE VIEW vw_sediment_priority AS


SELECT


    l.location_id,

    l.latitude,

    l.longitude,

    l.zone,

    l.watershed_id,


    ROUND(
        SUM(s.sediment_load_tons),
        2
    ) AS annual_sediment_load_tons,


    ROUND(
        AVG(s.sediment_risk_index),
        2
    ) AS average_sediment_risk,


    CASE

        WHEN AVG(s.sediment_risk_index) < 25
            THEN 'Low'

        WHEN AVG(s.sediment_risk_index) < 50
            THEN 'Moderate'

        WHEN AVG(s.sediment_risk_index) < 75
            THEN 'High'

        ELSE 'Critical'

    END AS sediment_priority


FROM fact_sediment_daily s


JOIN dim_location l

ON s.location_id = l.location_id


GROUP BY

    l.location_id;





-- =====================================================
-- 3. PORT VULNERABILITY VIEW
-- =====================================================


DROP VIEW IF EXISTS vw_port_vulnerability;


CREATE VIEW vw_port_vulnerability AS


WITH flood AS (

    SELECT

        location_id,

        AVG(flood_risk_index) AS avg_flood_risk

    FROM fact_hydrology_daily

    GROUP BY location_id

),


sediment AS (

    SELECT

        location_id,

        AVG(sediment_risk_index) AS avg_sediment_risk

    FROM fact_sediment_daily

    GROUP BY location_id

)


SELECT

    l.zone,

    ROUND(
        AVG(f.avg_flood_risk),
        2
    ) AS average_flood_risk,


    ROUND(
        AVG(s.avg_sediment_risk),
        2
    ) AS average_sediment_risk,


    ROUND(

        (
        AVG(f.avg_flood_risk)
        +
        AVG(s.avg_sediment_risk)
        ) / 2,

        2

    ) AS vulnerability_score


FROM dim_location l


JOIN flood f

ON l.location_id = f.location_id


JOIN sediment s

ON l.location_id = s.location_id


WHERE l.zone = 'Port'


GROUP BY l.zone;




-- =====================================================
-- 4. WATERSHED PERFORMANCE VIEW
-- =====================================================


DROP VIEW IF EXISTS vw_watershed_analysis;


CREATE VIEW vw_watershed_analysis AS


SELECT


    w.watershed_id,


    w.watershed_name,


    ROUND(
        AVG(h.flood_risk_index),
        2
    ) AS average_flood_risk,


    ROUND(
        SUM(s.sediment_load_tons),
        2
    ) AS total_sediment_load,


    ROUND(
        AVG(s.sediment_risk_index),
        2
    ) AS average_sediment_risk



FROM dim_watershed w


JOIN dim_location l

ON w.watershed_id = l.watershed_id


JOIN fact_hydrology_daily h

ON l.location_id = h.location_id


JOIN fact_sediment_daily s

ON l.location_id = s.location_id


GROUP BY

    w.watershed_id;