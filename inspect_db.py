import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Inspeccionar la tabla recursos
cursor.execute("PRAGMA table_info(recursos)")
schema = cursor.fetchall()

print("Esquema actual de la tabla 'recursos':")
for column in schema:
    print(column)

conn.close()