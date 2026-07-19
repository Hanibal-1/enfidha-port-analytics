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

l.zone,

l.watershed_id,

h.average_flood_risk,

h.maximum_flood_risk,

s.average_sediment_risk,

s.total_sediment_load


FROM dim_location l


JOIN hydro h

ON l.location_id=h.location_id


JOIN sediment s

ON l.location_id=s.location_id;