from fastapi import FastAPI, HTTPException, Request, Query
from database import create_tables, get_recursos, guardar_interaccion, insert_recurso
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from ai_model import (
    generar_respuesta_historia,
    generar_respuesta_recursos,
    generar_respuesta_formacion
)


# Configurar el directorio de templates
templates = Jinja2Templates(directory="templates")

# Crear las tablas al iniciar la aplicación
create_tables()

# Insertar datos iniciales al inicio
insert_recurso("Asociaciones", "Arcópoli: Asociación LGTB+ en Madrid", "https://arcopoli.org")
insert_recurso("Protocolos", "Protocolo de actuación ante agresiones", "https://ejemplo.com/protocolo")
insert_recurso("Educación", "Guía de lenguaje inclusivo", "https://ejemplo.com/guia")

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Página de inicio.
    """
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/recursos", response_class=HTMLResponse)
async def listar_recursos(request: Request, pregunta: str = Query(None)):
    """
    Página de Recursos LGTBI.
    """
    try:
        # Obtener recursos desde la base de datos
        recursos = get_recursos()
        
        if pregunta:
            # Generar respuesta para la pregunta
            respuesta = generar_respuesta_recursos(pregunta)
            
            # Guardar interacción en la base de datos
            guardar_interaccion("recursos", pregunta, respuesta)
            
            # Renderizar la plantilla con la respuesta generada
            return templates.TemplateResponse("recursos.html", {
                "request": request,
                "recursos": recursos,
                "respuesta": respuesta,
                "pregunta": pregunta
            })
        
        # Renderizar la plantilla sin consulta personalizada
        return templates.TemplateResponse("recursos.html", {
            "request": request,
            "recursos": recursos
        })

    except Exception as e:
        # Manejar errores inesperados
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")


@app.get("/historia", response_class=HTMLResponse)
async def historia(request: Request, opcion: str = Query(None), consulta: str = Query(None)):
    """
    Página de Historia LGTBI.
    """
    # Datos de ejemplo para los artículos destacados
    articulos = [
        {"titulo": "Los disturbios de Stonewall", "descripcion": "El inicio del movimiento moderno LGTBI."},
        {"titulo": "El primer Orgullo LGTBI", "descripcion": "Celebrado en 1970, un año después de Stonewall."},
        {"titulo": "Ley de Matrimonio Igualitario en España", "descripcion": "Aprobada en 2005."},
    ]

    if opcion:
        # Lógica para manejar "opción"
        respuesta = f"Explicación detallada sobre {opcion}."
        return templates.TemplateResponse("historia.html", {"request": request, "articulos": articulos, "respuesta": respuesta, "opcion": opcion})

    if consulta:
        # Lógica para manejar "consulta" con el modelo
        respuesta = generar_respuesta_historia(consulta)  # Usar el modelo para generar la respuesta
        return templates.TemplateResponse("historia.html", {"request": request, "articulos": articulos, "respuesta": respuesta, "consulta": consulta})

    # Si no hay ni opción ni consulta, renderizar la página principal de Historia
    return templates.TemplateResponse("historia.html", {"request": request, "articulos": articulos})

@app.get("/formacion")
def formacion(tema: str):
    """
    Endpoint para ofrecer formación sobre temas LGTBI.
    """
    if not tema:
        raise HTTPException(status_code=400, detail="El tema no puede estar vacío.")
    
    # Generar respuesta específica para formación
    respuesta = generar_respuesta_formacion(tema)
    return {"tema": tema, "respuesta": respuesta}