import sqlite3


DB = "data/warehouse/enfidha_port.db"


with open(
    "sql/risk_dimension.sql",
    "r"
) as file:

    sql = file.read()



conn = sqlite3.connect(DB)


conn.executescript(sql)


conn.close()


print(
    "Risk dimension created successfully"
)