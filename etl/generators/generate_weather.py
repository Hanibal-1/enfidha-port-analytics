import pandas as pd
import numpy as np


from config import (
    START_DATE,
    END_DATE,
    RANDOM_SEED
)


np.random.seed(RANDOM_SEED)



def seasonal_temperature(month):

    if month in [12,1,2]:

        return np.random.normal(
            14,
            3
        )

    elif month in [3,4,5]:

        return np.random.normal(
            20,
            4
        )

    elif month in [6,7,8]:

        return np.random.normal(
            31,
            3
        )

    else:

        return np.random.normal(
            24,
            4
        )



def seasonal_rainfall(month):


    if month in [11,12,1,2]:

        rainfall = np.random.gamma(
            2,
            12
        )


    elif month in [3,4,5,10]:

        rainfall = np.random.gamma(
            2,
            8
        )


    else:

        rainfall = np.random.gamma(
            1,
            1
        )


    # Extreme Mediterranean storm events

    if np.random.random() < 0.02:

        rainfall *= 5


    return round(
        rainfall,
        2
    )



def generate_weather():


    locations = pd.read_csv(
        "data/processed/spatial_locations.csv"
    )


    dates = pd.date_range(
        START_DATE,
        END_DATE,
        freq="D"
    )


    records = []

    weather_id = 1


    for date in dates:

        for location_id in locations.location_id:


            rainfall = seasonal_rainfall(
                date.month
            )


            temperature = seasonal_temperature(
                date.month
            )


            records.append({

                "weather_id":
                    weather_id,

                "date":
                    date.strftime(
                        "%Y-%m-%d"
                    ),

                "location_id":
                    location_id,

                "rainfall_mm":
                    rainfall,

                "temperature_c":
                    round(
                        temperature,
                        2
                    ),

                "humidity_pct":
                    round(
                        np.random.uniform(
                            45,
                            90
                        ),
                        2
                    ),

                "wind_speed_kmh":
                    round(
                        np.random.uniform(
                            5,
                            45
                        ),
                        2
                    ),

                "pressure_hpa":
                    round(
                        np.random.normal(
                            1013,
                            8
                        ),
                        2
                    )

            })


            weather_id += 1


    return pd.DataFrame(records)



if __name__ == "__main__":


    df = generate_weather()


    print("="*60)
    print("WEATHER FACT GENERATED")
    print("="*60)


    print(df.head())


    print()

    print(
        df.describe()
    )


    df.to_parquet(
        "data/raw/weather_daily.parquet",
        index=False
    )


    print()

    print(
        f"Generated {len(df)} weather records"
    )