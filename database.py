from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.sql import text
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

try:
    # Configurar la URL de conexión a la base de datos usando las variables del .env
    DATABASE_URL = f"mysql+pymysql://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}@" \
                   f"{os.getenv('DATABASE_HOST')}:{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_NAME')}"
    
    if not all([os.getenv('DATABASE_USER'), os.getenv('DATABASE_PASSWORD'), os.getenv('DATABASE_HOST'), 
                os.getenv('DATABASE_PORT'), os.getenv('DATABASE_NAME')]):
        raise ValueError("Faltan credenciales en el archivo .env para conectarse a la base de datos.")

    # Configurar el motor de la base de datos
    engine = create_engine(DATABASE_URL)
    metadata = MetaData()

except Exception as e:
    print(f"Error: {e}")
    print("Por favor, asegúrate de proporcionar las credenciales de la base de datos en un archivo .env.")
    exit()

# Definir las tablas
recursos = Table(
    "recursos",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("categoria", String(255), nullable=False),
    Column("descripcion", Text, nullable=False),
    Column("enlace", Text, nullable=False),
)

interacciones = Table(
    "interacciones",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("endpoint", String(255), nullable=False),
    Column("consulta", Text, nullable=False),
    Column("respuesta", Text, nullable=False),
    Column("metadata", Text, nullable=True),
    Column("timestamp", TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")),
)

# Crear las tablas en la base de datos si no existen
def create_tables():
    """
    Crea las tablas necesarias en la base de datos.
    """
    metadata.create_all(engine)
    print("Tablas creadas/verificadas correctamente.")

# Función para guardar una interacción
def guardar_interaccion(endpoint, consulta, respuesta, metadata="{}"):
    """
    Guarda una interacción en la base de datos.
    """
    with engine.connect() as conn:
        conn.execute(interacciones.insert().values(
            endpoint=endpoint,
            consulta=consulta,
            respuesta=respuesta,
            metadata=metadata
        ))
    print("Interacción guardada correctamente.")

# Función para obtener las últimas interacciones
def get_interacciones(limit=10):
    """
    Devuelve las últimas interacciones registradas en la base de datos.
    """
    with engine.connect() as conn:
        result = conn.execute(interacciones.select().order_by(interacciones.c.timestamp.desc()).limit(limit))
        interacciones_data = [
            {
                "id": row["id"],
                "endpoint": row["endpoint"],
                "consulta": row["consulta"],
                "respuesta": row["respuesta"],
                "metadata": row["metadata"],
                "timestamp": row["timestamp"]
            }
            for row in result
        ]
    return interacciones_data

# Función para obtener recursos
def get_recursos():
    """
    Devuelve una lista de recursos almacenados en la base de datos.
    """
    with engine.connect() as conn:
        result = conn.execute(recursos.select())
        recursos_data = [
            {"categoria": row["categoria"], "descripcion": row["descripcion"], "enlace": row["enlace"]}
            for row in result
        ]
    return recursos_data

# Función para insertar un recurso
def insert_recurso(categoria, descripcion, enlace):
    """
    Inserta un recurso en la tabla de recursos.
    """
    with engine.connect() as conn:
        conn.execute(recursos.insert().values(
            categoria=categoria,
            descripcion=descripcion,
            enlace=enlace
        ))
    print("Recurso insertado correctamente.")

# Función para eliminar interacciones antiguas
def delete_old_interacciones(days_old=30):
    """
    Elimina interacciones más antiguas que un número de días especificado.
    """
    with engine.connect() as conn:
        result = conn.execute(text(f"""
        DELETE FROM interacciones
        WHERE timestamp <= NOW() - INTERVAL {days_old} DAY
        """))
        deleted_rows = result.rowcount
    print(f"Interacciones eliminadas: {deleted_rows}")
    return {"deleted_rows": deleted_rows}

# Crear tablas automáticamente al iniciar
if __name__ == "__main__":
    create_tables()