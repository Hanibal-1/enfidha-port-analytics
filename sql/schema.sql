-- ============================================
-- ENFIDHA PORT ANALYTICS PLATFORM
-- Data Warehouse Schema
-- ============================================

PRAGMA foreign_keys = ON;

------------------------------------------------
-- DROP TABLES
------------------------------------------------

DROP TABLE IF EXISTS fact_engineering;
DROP TABLE IF EXISTS fact_sediment;
DROP TABLE IF EXISTS fact_flood_risk;
DROP TABLE IF EXISTS fact_hydrology;
DROP TABLE IF EXISTS fact_terrain;
DROP TABLE IF EXISTS fact_rainfall;
DROP TABLE IF EXISTS fact_weather;

DROP TABLE IF EXISTS dim_weather_station;
DROP TABLE IF EXISTS dim_location;
DROP TABLE IF EXISTS dim_date;

------------------------------------------------
-- DIM DATE
------------------------------------------------

CREATE TABLE dim_date (

    date_id INTEGER PRIMARY KEY,

    full_date DATE NOT NULL UNIQUE,

    day INTEGER,

    month INTEGER,

    month_name TEXT,

    quarter INTEGER,

    year INTEGER,

    season TEXT,

    week_of_year INTEGER,

    is_weekend INTEGER

);

------------------------------------------------
-- DIM LOCATION
------------------------------------------------

CREATE TABLE dim_location (

    location_id INTEGER PRIMARY KEY,

    latitude REAL NOT NULL,

    longitude REAL NOT NULL,

    elevation REAL,

    watershed TEXT,

    zone TEXT,

    soil_type TEXT,

    land_cover TEXT,

    distance_to_coast REAL

);

------------------------------------------------
-- DIM WEATHER STATION
------------------------------------------------

CREATE TABLE dim_weather_station (

    station_id INTEGER PRIMARY KEY,

    station_name TEXT,

    latitude REAL,

    longitude REAL,

    elevation REAL

);

------------------------------------------------
-- FACT WEATHER
------------------------------------------------

CREATE TABLE fact_weather (

    weather_id INTEGER PRIMARY KEY AUTOINCREMENT,

    date_id INTEGER,

    station_id INTEGER,

    temperature REAL,

    humidity REAL,

    wind_speed REAL,

    pressure REAL,

    solar_radiation REAL,

    FOREIGN KEY(date_id)
        REFERENCES dim_date(date_id),

    FOREIGN KEY(station_id)
        REFERENCES dim_weather_station(station_id)

);

------------------------------------------------
-- FACT RAINFALL
------------------------------------------------

CREATE TABLE fact_rainfall (

    rainfall_id INTEGER PRIMARY KEY AUTOINCREMENT,

    date_id INTEGER,

    location_id INTEGER,

    rainfall_mm REAL,

    rainfall_intensity REAL,

    storm_event INTEGER,

    FOREIGN KEY(date_id)
        REFERENCES dim_date(date_id),

    FOREIGN KEY(location_id)
        REFERENCES dim_location(location_id)

);

------------------------------------------------
-- FACT TERRAIN
------------------------------------------------

CREATE TABLE fact_terrain (

    terrain_id INTEGER PRIMARY KEY AUTOINCREMENT,

    location_id INTEGER,

    slope REAL,

    aspect REAL,

    curvature REAL,

    hillshade REAL,

    FOREIGN KEY(location_id)
        REFERENCES dim_location(location_id)

);

------------------------------------------------
-- FACT HYDROLOGY
------------------------------------------------

CREATE TABLE fact_hydrology (

    hydro_id INTEGER PRIMARY KEY AUTOINCREMENT,

    date_id INTEGER,

    location_id INTEGER,

    runoff REAL,

    infiltration REAL,

    drainage_density REAL,

    flow_accumulation REAL,

    FOREIGN KEY(date_id)
        REFERENCES dim_date(date_id),

    FOREIGN KEY(location_id)
        REFERENCES dim_location(location_id)

);

------------------------------------------------
-- FACT FLOOD RISK
------------------------------------------------

CREATE TABLE fact_flood_risk (

    flood_id INTEGER PRIMARY KEY AUTOINCREMENT,

    date_id INTEGER,

    location_id INTEGER,

    rainfall_mm REAL,

    runoff REAL,

    slope REAL,

    flood_index REAL,

    flood_depth REAL,

    flood_probability REAL,

    risk_level TEXT,

    FOREIGN KEY(date_id)
        REFERENCES dim_date(date_id),

    FOREIGN KEY(location_id)
        REFERENCES dim_location(location_id)

);

------------------------------------------------
-- FACT SEDIMENT
------------------------------------------------

CREATE TABLE fact_sediment (

    sediment_id INTEGER PRIMARY KEY AUTOINCREMENT,

    date_id INTEGER,

    location_id INTEGER,

    erosion_rate REAL,

    sediment_load REAL,

    sediment_risk REAL,

    FOREIGN KEY(date_id)
        REFERENCES dim_date(date_id),

    FOREIGN KEY(location_id)
        REFERENCES dim_location(location_id)

);

------------------------------------------------
-- FACT ENGINEERING
------------------------------------------------

CREATE TABLE fact_engineering (

    engineering_id INTEGER PRIMARY KEY AUTOINCREMENT,

    date_id INTEGER,

    location_id INTEGER,

    construction_risk REAL,

    maintenance_index REAL,

    dredging_volume REAL,

    engineering_score REAL,

    FOREIGN KEY(date_id)
        REFERENCES dim_date(date_id),

    FOREIGN KEY(location_id)
        REFERENCES dim_location(location_id)

);