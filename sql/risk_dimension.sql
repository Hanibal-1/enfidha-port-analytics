DROP TABLE IF EXISTS dim_risk_threshold;


CREATE TABLE dim_risk_threshold (

    risk_level TEXT PRIMARY KEY,

    min_score REAL,

    max_score REAL,

    description TEXT

);



INSERT INTO dim_risk_threshold VALUES

(
    'Low',
    0,
    25,
    'Low environmental and engineering concern'
),


(
    'Moderate',
    25,
    50,
    'Requires monitoring and preventive actions'
),


(
    'High',
    50,
    75,
    'Requires mitigation planning'
),


(
    'Critical',
    75,
    100,
    'Immediate engineering attention required'
);