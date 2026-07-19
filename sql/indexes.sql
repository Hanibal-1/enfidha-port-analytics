-- ==========================
-- WEATHER INDEXES
-- ==========================

CREATE INDEX IF NOT EXISTS idx_weather_location
ON fact_weather_daily(location_id);


CREATE INDEX IF NOT EXISTS idx_weather_date
ON fact_weather_daily(date);



-- ==========================
-- HYDROLOGY INDEXES
-- ==========================

CREATE INDEX IF NOT EXISTS idx_hydrology_location
ON fact_hydrology_daily(location_id);


CREATE INDEX IF NOT EXISTS idx_hydrology_date
ON fact_hydrology_daily(date);



-- ==========================
-- SEDIMENT INDEXES
-- ==========================

CREATE INDEX IF NOT EXISTS idx_sediment_location
ON fact_sediment_daily(location_id);


CREATE INDEX IF NOT EXISTS idx_sediment_date
ON fact_sediment_daily(date);



-- ==========================
-- RISK INDEXES
-- ==========================

CREATE INDEX IF NOT EXISTS idx_risk_location
ON fact_risk_assessment(location_id);


CREATE INDEX IF NOT EXISTS idx_risk_date
ON fact_risk_assessment(date);



-- ==========================
-- DIMENSION INDEXES
-- ==========================

CREATE INDEX IF NOT EXISTS idx_location_zone
ON dim_location(zone);


CREATE INDEX IF NOT EXISTS idx_location_watershed
ON dim_location(watershed_id);