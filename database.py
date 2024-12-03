from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.sql import text
from dotenv import load_dotenv
import os

load_dotenv()

# print("DATABASE_USER:", os.getenv("DATABASE_USER"))
# print("DATABASE_PASSWORD:", os.getenv("DATABASE_PASSWORD"))
# print("DATABASE_HOST:", os.getenv("DATABASE_HOST"))
# print("DATABASE_PORT:", os.getenv("DATABASE_PORT"))
# print("DATABASE_NAME:", os.getenv("DATABASE_NAME"))

try:
    DATABASE_URL = f"mysql+pymysql://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}@" \
                   f"{os.getenv('DATABASE_HOST')}:{os.getenv('DATABASE_PORT')}/information_schema"
    print("Intentando conectar a la base de datos")
    
    engine = create_engine(DATABASE_URL)
    
    with engine.connect() as conn:
        result = conn.execute(text("SHOW DATABASES;"))
        databases = [row[0] for row in result]
        if os.getenv("DATABASE_NAME") not in databases:
            print(f"Base de datos '{os.getenv('DATABASE_NAME')}' no encontrada. Creándola...")
            conn.execute(text(f"CREATE DATABASE {os.getenv('DATABASE_NAME')}"))
            print(f"Base de datos '{os.getenv('DATABASE_NAME')}' creada exitosamente.")
        else:
            print(f"Base de datos '{os.getenv('DATABASE_NAME')}' ya existe.")
except Exception as e:
    print(f"Error al conectar o verificar la base de datos: {e}")
    exit()

try:
    DATABASE_URL = f"mysql+pymysql://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}@" \
                   f"{os.getenv('DATABASE_HOST')}:{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_NAME')}"
    engine = create_engine(DATABASE_URL)
    metadata = MetaData()
    print("¡Conexión exitosa a la base de datos final!")
except Exception as e:
    print(f"Error al conectar con la base de datos especificada: {e}")
    exit()

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

def create_tables():
    """
    Crea las tablas necesarias en la base de datos.
    """
    try:
        metadata.create_all(engine)
        print("Tablas creadas/verificadas correctamente.")
    except Exception as e:
        print(f"Error al crear las tablas: {e}")

def guardar_interaccion(endpoint, consulta, respuesta, metadata="{}"):
    """
    Guarda una interacción en la base de datos.
    """
    try:
        with engine.connect() as conn:
            conn.execute(interacciones.insert().values(
                endpoint=endpoint,
                consulta=consulta,
                respuesta=respuesta,
                metadata=metadata
            ))
        print("Interacción guardada correctamente.")
    except Exception as e:
        print(f"Error al guardar la interacción: {e}")

def get_interacciones(limit=10):
    """
    Devuelve las últimas interacciones registradas en la base de datos.
    """
    try:
        with engine.connect() as conn:
            result = conn.execute(interacciones.select().order_by(interacciones.c.timestamp.desc()).limit(limit))
            return [
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
    except Exception as e:
        print(f"Error al obtener las interacciones: {e}")
        return []

def get_recursos():
    """
    Devuelve una lista de recursos almacenados en la base de datos.
    """
    try:
        with engine.connect() as conn:
            result = conn.execute(recursos.select())
            return [
                {"categoria": row["categoria"], "descripcion": row["descripcion"], "enlace": row["enlace"]}
                for row in result
            ]
    except Exception as e:
        print(f"Error al obtener recursos: {e}")
        return []

if __name__ == "__main__":
    create_tables()