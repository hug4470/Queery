from fastapi import FastAPI, HTTPException
from ai_model import (
    generar_respuesta_historia,
    generar_respuesta_recursos,
    generar_respuesta_formacion
)
from database import create_tables, get_recursos, insert_recurso

# Crear las tablas al iniciar la aplicación
create_tables()

# Insertar datos iniciales al inicio
insert_recurso("Asociaciones", "Arcópoli: Asociación LGTB+ en Madrid", "https://arcopoli.org")
insert_recurso("Protocolos", "Protocolo de actuación ante agresiones", "https://ejemplo.com/protocolo")
insert_recurso("Educación", "Guía de lenguaje inclusivo", "https://ejemplo.com/guia")

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "¡Hola, mundo!"}

@app.get("/recursos")
async def listar_recursos(pregunta: str = None):
    """
    Endpoint para listar recursos o responder preguntas relacionadas con ellos.
    """
    if pregunta:
        # Generar respuesta específica para recursos
        respuesta = generar_respuesta_recursos(pregunta)
        return {"pregunta": pregunta, "respuesta": respuesta}
    
    # Si no hay pregunta, mostrar los recursos almacenados
    recursos = get_recursos()
    return {"recursos": recursos}

@app.get("/historia")
async def historia(opcion: str = None, consulta: str = None):
    """
    Endpoint para consultar sobre historia LGTBI.
    """
    # Artículos principales
    articulos = [
        {"titulo": "Los disturbios de Stonewall", "descripcion": "El inicio del movimiento moderno LGTBI."},
        {"titulo": "El primer Orgullo LGTBI", "descripcion": "Celebrado en 1970, un año después de Stonewall."},
        {"titulo": "Ley de Matrimonio Igualitario en España", "descripcion": "Aprobada en 2005."},
    ]
    
    if opcion:
        # Generar respuesta específica para la opción seleccionada
        respuesta = generar_respuesta_historia(f"Explica más sobre: {opcion}")
        return {"opcion": opcion, "respuesta": respuesta}
    
    if consulta:
        # Si la consulta es un año, ajusta el prompt
        if consulta.isdigit():
            prompt = f"Habla sobre eventos LGTBI en el año {consulta}."
        else:
            prompt = f"Consulta histórica sobre LGTBI: {consulta}"
        respuesta = generar_respuesta_historia(prompt)
        return {"consulta": consulta, "respuesta": respuesta}
    
    # Si no se pasa ni opción ni consulta, devolver artículos principales
    return {"articulos": articulos}

@app.get("/formacion")
async def formacion(tema: str):
    """
    Endpoint para ofrecer formación sobre temas LGTBI.
    """
    if not tema:
        raise HTTPException(status_code=400, detail="El tema no puede estar vacío.")
    
    # Generar respuesta específica para formación
    respuesta = generar_respuesta_formacion(tema)
    return {"tema": tema, "respuesta": respuesta}