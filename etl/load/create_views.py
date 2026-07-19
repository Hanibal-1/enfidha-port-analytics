import sqlite3


DB = "data/warehouse/enfidha_port.db"


with open(
    "sql/analytics_views.sql",
    "r"
) as file:

    sql = file.read()



conn = sqlite3.connect(DB)


conn.executescript(sql)


conn.close()


print("Analytics views created successfully")