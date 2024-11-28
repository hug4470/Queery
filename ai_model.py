import google.generativeai as genai
import os
gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)

if not gemini_api_key:
    raise EnvironmentError("La variable GEMINI_API_KEY no está configurada o es inválida.")

def generar_respuesta_historia(prompt):
    """
    Genera respuestas personalizadas para el endpoint de Historia.
    """
    prompt_historia = f"Solo en referente a histórico LGTBI, si procede (si no, pide más especificidad), responde: {prompt}"
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt_historia)
        return response.text
    except Exception as e:
        return f"Error al generar respuesta para historia: {str(e)}"

def generar_respuesta_recursos(prompt):
    """
    Genera respuestas personalizadas para el endpoint de Recursos.
    """
    prompt_recursos = f"Sobre recursos LGTBI, responde: {prompt}"
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt_recursos)
        return response.text
    except Exception as e:
        return f"Error al generar respuesta para recursos: {str(e)}"

def generar_respuesta_formacion(prompt):
    """
    Genera respuestas personalizadas para el endpoint de Formación.
    """
    prompt_formacion = f"Ofrece una explicación educativa en materia LGTBI muy bien documentada y con recursos: {prompt}"
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt_formacion)
        return response.text
    except Exception as e:
        return f"Error al generar respuesta para formación: {str(e)}"