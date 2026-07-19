import sqlite3

DB = "data/warehouse/enfidha_port.db"

conn = sqlite3.connect(DB)

cursor = conn.cursor()

print("=" * 60)
print("CREATING CLIMATE REPORTING VIEWS")
print("=" * 60)

# ==========================================================
# WEATHER MONTHLY
# ==========================================================

cursor.execute("""

DROP VIEW IF EXISTS vw_weather_monthly;

""")

cursor.execute("""

CREATE VIEW vw_weather_monthly AS

SELECT

    substr(date,1,4) AS year,

    substr(date,6,2) AS month,

    ROUND(AVG(rainfall_mm),2) AS avg_rainfall,

    ROUND(AVG(temperature_c),2) AS avg_temperature,

    ROUND(AVG(wind_speed_kmh),2) AS avg_wind_speed

FROM fact_weather_daily

GROUP BY

    substr(date,1,4),

    substr(date,6,2)

ORDER BY

    year,

    month;

""")

print("✓ vw_weather_monthly created")

# ==========================================================
# HYDROLOGY MONTHLY
# ==========================================================

cursor.execute("""

DROP VIEW IF EXISTS vw_hydrology_monthly;

""")

cursor.execute("""

CREATE VIEW vw_hydrology_monthly AS

SELECT

    substr(date,1,4) AS year,

    substr(date,6,2) AS month,

    ROUND(AVG(runoff_mm),2) AS avg_runoff,

    ROUND(AVG(runoff_volume_m3),2) AS avg_runoff_volume,

    ROUND(AVG(flood_risk_index),2) AS avg_flood_risk

FROM fact_hydrology_daily

GROUP BY

    substr(date,1,4),

    substr(date,6,2)

ORDER BY

    year,

    month;

""")

print("✓ vw_hydrology_monthly created")

conn.commit()
conn.close()

print()
print("Climate reporting views created successfully.")