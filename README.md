# 🚢 Enfidha Port Engineering Analytics Platform

> **End-to-End Geospatial Engineering Decision Support Platform for Flood Risk, Hydrology, Sediment Transport, and Infrastructure Planning**

---

## 📌 Project Overview

The **Enfidha Port Engineering Analytics Platform** is an end-to-end geospatial analytics solution designed to support infrastructure planning and environmental risk assessment for the future **Enfidha Deep Water Port (Tunisia)**.

The platform combines **Data Engineering, GIS, Hydrology, Environmental Analytics, and Business Intelligence** into a unified decision-support system that helps engineers identify flood-prone areas, evaluate sediment transport, and prioritize infrastructure investments.

Unlike traditional dashboards, this project follows a complete analytics lifecycle:

* Data Engineering
* ETL Pipelines
* Synthetic Environmental Data Generation
* Spatial Analytics
* Hydrological Modeling
* Data Warehouse Design
* Power BI Dashboard Development
* Executive Decision Support

---

# 🎯 Project Objectives

The platform was developed to answer critical engineering questions such as:

* Which areas around the port are most exposed to flooding?
* Where is sediment accumulation likely to increase dredging requirements?
* Which watersheds contribute most to flood risk?
* How can engineering teams prioritize mitigation efforts?
* Which locations require immediate infrastructure intervention?

---

# 🏗️ System Architecture

```text
                           Environmental Data
                                     │
        ┌────────────────────────────┼────────────────────────────┐
        │                            │                            │
        ▼                            ▼                            ▼
 Weather Generator          Spatial Generator         Hydrology Generator
        │                            │                            │
        └────────────────────────────┼────────────────────────────┘
                                     ▼
                           Data Transformation
                                     │
                                     ▼
                              SQLite Warehouse
                                     │
                    ┌────────────────┼────────────────┐
                    ▼                ▼                ▼
            Analytics Tables    SQL Views      KPI Calculations
                    │                │                │
                    └────────────────┼────────────────┘
                                     ▼
                           Power BI Dashboard
                                     │
                                     ▼
                    Engineering Decision Support
```

---

# 📂 Project Structure

```text
enfidha-port-analytics/

├── analytics/
├── app/
├── data/
│   ├── raw/
│   ├── processed/
│   ├── warehouse/
│   └── exports/
├── docs/
├── etl/
│   ├── extract/
│   ├── generators/
│   ├── transform/
│   ├── validation/
│   └── load/
├── sql/
├── tests/
├── README.md
├── requirements.txt
└── .gitignore
```

---

# ⚙️ Technology Stack

| Category           | Technologies            |
| ------------------ | ----------------------- |
| Programming        | Python                  |
| Database           | SQLite                  |
| Data Processing    | Pandas, NumPy           |
| Spatial Analytics  | Synthetic GIS Model     |
| BI & Visualization | Power BI                |
| SQL                | SQLite SQL              |
| ETL                | Custom Python Pipelines |
| Version Control    | Git & GitHub            |

---

# 📊 Data Warehouse

The warehouse follows a dimensional model with analytical fact tables.

## Dimension Tables

* dim_location
* dim_soil
* dim_landcover
* dim_watershed
* dim_risk_threshold

## Fact Tables

* fact_weather_daily
* fact_hydrology_daily
* fact_sediment_daily
* fact_risk_assessment

## Analytics Tables

* agg_location_risk

## Reporting Views

* vw_port_summary
* vw_flood_risk_map
* vw_sediment_risk_map
* vw_zone_analysis
* vw_weather_monthly
* vw_hydrology_monthly

---

# ⚡ ETL Pipeline

```text
Generate Spatial Data
        │
Generate Weather
        │
Generate Hydrology
        │
Generate Sediment
        │
Generate Risk Assessment
        │
Load Data Warehouse
        │
Create Analytics Views
        │
Export Power BI Dataset
```

---

# 🌍 Spatial Engineering Model

The synthetic spatial model represents the Enfidha Port study area using **2,500 engineering analysis cells**.

Each location contains:

* Latitude
* Longitude
* Elevation
* Terrain Slope
* Distance to Port
* Distance to Coast
* Land Zone
* Watershed
* Flood Risk
* Sediment Risk

Study Area Categories:

* Port
* Coastal
* Wetland
* Agriculture
* Hills

---

# 📈 Power BI Dashboard

The solution includes a multi-page executive dashboard.

## Executive Overview

* Engineering KPIs
* Flood Risk Summary
* Sediment Risk Summary
* Overall Vulnerability
* Zone Comparison

---

## Spatial Risk Intelligence

* Azure Maps
* Flood Risk Map
* Sediment Risk Map
* High Risk Locations
* Spatial Hotspots

---

## Climate & Hydrological Analytics

* Rainfall Trends
* Runoff Trends
* Flood Risk Evolution
* Seasonal Analysis
* Hydrological KPIs

---

## Infrastructure Planning

* Engineering Priority Matrix
* Risk-Based Decision Support
* Infrastructure Recommendations
* Priority Locations
* Executive Summary

---

# 📷 Dashboard Preview

> Add screenshots here after exporting from Power BI.

![alt text](image-6.png)


```
docs/screenshots/

01_Executive_Overview.png 

02_Spatial_Risk_Intelligence.png


03_Climate_Analytics.png


04_Infrastructure_Planning.png

```

---

# 📊 Key Engineering KPIs

* Total Spatial Cells Analysed
* Average Flood Risk
* Maximum Flood Risk
* Average Sediment Risk
* Maximum Sediment Risk
* Total Sediment Load
* Engineering Vulnerability Score
* High Risk Locations

---

# 🚀 Key Features

* End-to-End ETL Pipeline
* Engineering Data Warehouse
* Synthetic Environmental Data Generator
* Hydrological Risk Assessment
* Flood Risk Modeling
* Sediment Transport Analysis
* GIS-Based Spatial Intelligence
* Power BI Executive Dashboard
* Engineering Decision Support
* Automated KPI Generation

---

# 🧪 Validation

The project includes automated validation scripts for:

* Spatial Data Validation
* Data Quality Checks
* Warehouse Validation
* Analytics Validation
* SQL View Validation

---

# 💼 Business Value

This platform demonstrates how modern data engineering and business intelligence techniques can support engineering decision-making by:

* Monitoring environmental risks
* Supporting infrastructure planning
* Prioritizing engineering interventions
* Improving flood preparedness
* Optimizing dredging operations
* Delivering executive-level reporting

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/enfidha-port-analytics.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the ETL pipeline:

```bash
python etl/load/create_warehouse.py
python etl/load/load_warehouse.py
python etl/load/create_analytics_tables.py
python etl/load/create_bi_views.py
python etl/export/export_powerbi.py
```

---

# 🔮 Future Improvements

* Integration with real ERA5 and CHIRPS climate datasets
* Satellite imagery analysis
* Machine Learning flood prediction
* Real-time IoT sensor integration
* Web GIS dashboard
* Predictive maintenance analytics
* Climate change scenario simulation

---

# 👨‍💻 Author

**Houcine Ben Romdhane**

Data Analyst | Business Intelligence | Data Engineering | GIS Analytics | Python | SQL | Power BI

---

## ⭐ If you found this project interesting, consider giving it a star!
