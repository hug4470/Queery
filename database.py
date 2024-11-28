import sqlite3

def create_tables():
    """
    Crea las tablas necesarias en la base de datos.
    """
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    # Crear tabla de recursos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS recursos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        categoria TEXT NOT NULL,
        descripcion TEXT NOT NULL,
        enlace TEXT NOT NULL
    )
    """)

    # Crear tabla para registrar interacciones
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS interacciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        endpoint TEXT NOT NULL,
        consulta TEXT NOT NULL,
        respuesta TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    conn.commit()
    conn.close()


def guardar_interaccion(endpoint, consulta, respuesta):
    """
    Guarda una interacción en la base de datos.
    """
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO interacciones (endpoint, consulta, respuesta)
    VALUES (?, ?, ?)
    """, (endpoint, consulta, respuesta))
    conn.commit()
    conn.close()


def get_recursos():
    """
    Devuelve una lista de recursos almacenados en la base de datos.
    """
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT categoria, descripcion, enlace FROM recursos")
    recursos = [{"categoria": row[0], "descripcion": row[1], "enlace": row[2]} for row in cursor.fetchall()]
    conn.close()
    return recursos


def insert_recurso(categoria, descripcion, enlace):
    """
    Inserta un recurso en la tabla de recursos.
    """
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO recursos (categoria, descripcion, enlace)
    VALUES (?, ?, ?)
    """, (categoria, descripcion, enlace))
    conn.commit()
    conn.close()