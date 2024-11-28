import sqlite3

DATABASE_NAME = "database.db"

def create_tables():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS recursos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        categoria TEXT NOT NULL,
        descripcion TEXT,
        enlace TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS consultas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo TEXT NOT NULL,
        consulta TEXT NOT NULL,
        respuesta TEXT
    )
    """)
    conn.commit()
    conn.close()

def insert_recurso(categoria, descripcion, enlace):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
    SELECT * FROM recursos WHERE descripcion = ? AND enlace = ?
    """, (descripcion, enlace))
    resultado = cursor.fetchone()
    
    if resultado is None:
        # Si no existe, insertar el recurso
        cursor.execute("""
        INSERT INTO recursos (categoria, descripcion, enlace)
        VALUES (?, ?, ?)
        """, (categoria, descripcion, enlace))
        conn.commit()
    conn.close()

def get_recursos():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM recursos")
    recursos = cursor.fetchall()
    conn.close()
    return recursos