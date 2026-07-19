import sqlite3


DB = "data/warehouse/enfidha_port.db"


with open(
    "sql/warehouse_schema.sql",
    "r"
) as file:

    schema = file.read()



conn = sqlite3.connect(DB)


conn.executescript(schema)


conn.close()


print("Warehouse schema created successfully")