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



DROP VIEW IF EXISTS vw_sediment_risk_map;


CREATE VIEW vw_sediment_risk_map AS


SELECT

location_id,

latitude,

longitude,

zone,

total_sediment_load,

average_sediment_risk,

sediment_risk_level


FROM agg_location_risk;


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
(average_flood_risk + average_sediment_risk)/2
),
2
) AS vulnerability_score,


COUNT(*) AS locations


FROM agg_location_risk


WHERE zone='Port'


GROUP BY zone;






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