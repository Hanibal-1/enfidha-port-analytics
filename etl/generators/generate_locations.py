import pandas as pd
import numpy as np
from math import radians, sin, cos, sqrt, atan2

from config import (
    PORT_LATITUDE,
    PORT_LONGITUDE,
    LAT_MIN,
    LAT_MAX,
    LON_MIN,
    LON_MAX,
    GRID_ROWS,
    GRID_COLS,
    RANDOM_SEED
)


np.random.seed(RANDOM_SEED)


# ==========================================
# Distance calculation
# ==========================================

def haversine(lat1, lon1, lat2, lon2):

    R = 6371

    lat1 = radians(lat1)
    lon1 = radians(lon1)

    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        sin(dlat / 2) ** 2
        +
        cos(lat1)
        *
        cos(lat2)
        *
        sin(dlon / 2) ** 2
    )

    c = 2 * atan2(
        sqrt(a),
        sqrt(1-a)
    )

    return R * c


# ==========================================
# Synthetic coastline model
# ==========================================

def distance_to_coast(lon):

    # Mediterranean coast approximately east
    coast_line = 10.50

    distance = abs(
        coast_line - lon
    )

    # convert degrees longitude to km
    return distance * 90


# ==========================================
# Synthetic DEM
# ==========================================

def generate_elevation(lat, lon):


    coast_distance = distance_to_coast(lon)


    # Coastal elevation increase
    elevation = coast_distance * 3


    # Inland terrain rise
    inland_factor = (
        (LON_MAX - lon)
        /
        (LON_MAX - LON_MIN)
    )


    elevation += inland_factor * 25


    # Southwest hills
    hill_effect = (
        max(0, LAT_MIN + 0.04 - lat)
        *
        250
    )

    elevation += hill_effect


    # Natural terrain variation

    variation = (
        np.sin(lat * 150)
        *
        np.cos(lon * 120)
        *
        5
    )

    elevation += variation


    # Coastal wetlands

    if coast_distance < 3:

        elevation -= 3


    return round(
        max(elevation,0),
        2
    )


# ==========================================
# Elevation category
# ==========================================

def elevation_category(elevation):

    if elevation < 2:
        return "Sea Level"

    elif elevation < 10:
        return "Low Coastal"

    elif elevation < 30:
        return "Coastal Plain"

    elif elevation < 70:
        return "Inland"

    else:
        return "High Terrain"


# ==========================================
# Synthetic slope model
# ==========================================

def generate_slope(elevation, zone=None):

    if elevation < 5:
        slope = np.random.uniform(0, 2)

    elif elevation < 30:
        slope = np.random.uniform(2, 8)

    elif elevation < 70:
        slope = np.random.uniform(5, 15)

    else:
        slope = np.random.uniform(10, 25)


    return round(slope, 2)


# ==========================================
# Zone classification
# ==========================================

def classify_zone(
        lat,
        lon,
        elevation
):

    port_distance = haversine(
        lat,
        lon,
        PORT_LATITUDE,
        PORT_LONGITUDE
    )


    if port_distance < 2:
        return "Port"


    elif elevation < 5:
        return "Wetland"


    elif elevation < 15:
        return "Coastal"


    elif elevation < 50:
        return "Agriculture"


    else:
        return "Hills"



# ==========================================
# Generate spatial grid
# ==========================================

def generate_locations():

    locations = []

    location_id = 1


    latitudes = np.linspace(
        LAT_MIN,
        LAT_MAX,
        GRID_ROWS
    )


    longitudes = np.linspace(
        LON_MIN,
        LON_MAX,
        GRID_COLS
    )


    for lat in latitudes:

        for lon in longitudes:


            elevation = generate_elevation(
                lat,
                lon
            )

            slope = generate_slope(
                elevation
            )

            port_distance = haversine(
                lat,
                lon,
                PORT_LATITUDE,
                PORT_LONGITUDE
            )


            coast_distance = distance_to_coast(
                lon
            )


            locations.append({

                "location_id":
                    location_id,

                "latitude":
                    round(lat,6),

                "longitude":
                    round(lon,6),

                "elevation_m":
                    elevation,

                "slope_degree":
                    slope,

                "elevation_category":
                    elevation_category(
                        elevation
                    ),

                "distance_to_port_km":
                    round(
                        port_distance,
                        2
                    ),

                "distance_to_coast_km":
                    round(
                        coast_distance,
                        2
                    ),

                "zone":
                    classify_zone(
                        lat,
                        lon,
                        elevation
                    )

            })


            location_id += 1


    return pd.DataFrame(locations)



if __name__ == "__main__":


    df = generate_locations()


    print("="*60)
    print("ENFIDHA SYNTHETIC SPATIAL MODEL")
    print("="*60)


    print(df.head())


    print("\nElevation statistics")

    print(
        df.elevation_m.describe()
    )


    print("\nZone distribution")

    print(
        df.zone.value_counts()
    )


    df.to_csv(
        "data/raw/location_grid.csv",
        index=False
    )


    print(
        f"\nGenerated {len(df)} spatial cells"
    )