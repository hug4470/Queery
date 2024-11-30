from fastapi import FastAPI, HTTPException, Request, Query
from database import create_tables, get_recursos, guardar_interaccion
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from ai_model import (
    generar_respuesta_historia,
    generar_respuesta_recursos,
    generar_respuesta_formacion,
)

# Configurar el directorio de templates
templates = Jinja2Templates(directory="templates")

# Crear las tablas al iniciar la aplicación
try:
    create_tables()
    print("Tablas creadas/verificadas correctamente.")
except Exception as e:
    print(f"Error al crear/verificar tablas: {e}")
    exit()

# Crear la aplicación FastAPI
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
                "pregunta": pregunta,
            })
        
        # Renderizar la plantilla sin consulta personalizada
        return templates.TemplateResponse("recursos.html", {
            "request": request,
            "recursos": recursos,
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

    try:
        if opcion:
            # Lógica para manejar "opción"
            respuesta = f"Explicación detallada sobre {opcion}."
            return templates.TemplateResponse("historia.html", {
                "request": request,
                "articulos": articulos,
                "respuesta": respuesta,
                "opcion": opcion,
            })

        if consulta:
            # Lógica para manejar "consulta" con el modelo
            respuesta = generar_respuesta_historia(consulta)
            return templates.TemplateResponse("historia.html", {
                "request": request,
                "articulos": articulos,
                "respuesta": respuesta,
                "consulta": consulta,
            })

        # Renderizar la página principal de Historia
        return templates.TemplateResponse("historia.html", {"request": request, "articulos": articulos})

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")

@app.get("/formacion", response_class=HTMLResponse)
async def listar_formacion(request: Request, tema: str = Query(None)):
    """
    Página de Formación LGTBI.
    """
    formaciones_destacadas = [
        {"titulo": "Uso correcto de pronombres", "descripcion": "Aprende a respetar las identidades de género."},
        {"titulo": "Lenguaje inclusivo", "descripcion": "Guía práctica para un lenguaje no discriminatorio."},
        {"titulo": "Apoyo a personas trans", "descripcion": "Cómo ser un buen aliado del colectivo trans."},
    ]

    try:
        if tema:
            # Generar respuesta para el tema solicitado
            respuesta = generar_respuesta_formacion(tema)
            
            # Guardar interacción en la base de datos
            guardar_interaccion("formacion", tema, respuesta)
            
            # Renderizar la plantilla con la respuesta generada
            return templates.TemplateResponse("formacion.html", {
                "request": request,
                "formaciones_destacadas": formaciones_destacadas,
                "respuesta": respuesta,
                "tema": tema,
            })

        # Renderizar la plantilla sin consulta personalizada
        return templates.TemplateResponse("formacion.html", {
            "request": request,
            "formaciones_destacadas": formaciones_destacadas,
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")