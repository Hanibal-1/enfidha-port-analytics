DROP TABLE IF EXISTS dim_location;

CREATE TABLE dim_location (

    location_id INTEGER PRIMARY KEY,

    latitude REAL,

    longitude REAL,

    elevation_m REAL,

    slope_degree REAL,

    zone TEXT,

    soil_id INTEGER,

    landcover_id INTEGER,

    watershed_id INTEGER

);


DROP TABLE IF EXISTS dim_soil;

CREATE TABLE dim_soil (

    soil_id INTEGER PRIMARY KEY,

    soil_name TEXT,

    permeability REAL,

    runoff_coefficient REAL,

    erosion_factor REAL,

    stability_factor REAL

);



DROP TABLE IF EXISTS dim_landcover;

CREATE TABLE dim_landcover (

    landcover_id INTEGER PRIMARY KEY,

    landcover_name TEXT,

    runoff_factor REAL,

    infiltration_factor REAL,

    roughness_factor REAL,

    engineering_factor REAL

);



DROP TABLE IF EXISTS dim_watershed;

CREATE TABLE dim_watershed (

    watershed_id INTEGER PRIMARY KEY,

    watershed_name TEXT,

    area_km2 REAL,

    stream_order INTEGER,

    outlet_latitude REAL,

    outlet_longitude REAL

);



DROP TABLE IF EXISTS fact_weather_daily;


CREATE TABLE fact_weather_daily (

    weather_id INTEGER PRIMARY KEY,

    date TEXT,

    location_id INTEGER,

    rainfall_mm REAL,

    temperature_c REAL,

    humidity_pct REAL,

    wind_speed_kmh REAL,

    pressure_hpa REAL

);



DROP TABLE IF EXISTS fact_hydrology_daily;


CREATE TABLE fact_hydrology_daily (

    hydrology_id INTEGER PRIMARY KEY,

    date TEXT,

    location_id INTEGER,

    runoff_mm REAL,

    runoff_volume_m3 REAL,

    flood_risk_index REAL

);



DROP TABLE IF EXISTS fact_sediment_daily;


CREATE TABLE fact_sediment_daily (

    sediment_id INTEGER PRIMARY KEY,

    date TEXT,

    location_id INTEGER,

    sediment_load_tons REAL,

    sediment_risk_index REAL

);



DROP TABLE IF EXISTS fact_risk_assessment;


CREATE TABLE fact_risk_assessment (

    risk_id INTEGER PRIMARY KEY,

    date TEXT,

    location_id INTEGER,

    flood_risk_level TEXT,

    sediment_risk_level TEXT

);