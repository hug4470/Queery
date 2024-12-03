import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

try:
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    
    if not gemini_api_key:
        raise ValueError("No utilices formato Markdown ni negrita, texto limpio. La variable GEMINI_API_KEY no está definida. Verifica tu archivo .env o las variables de entorno.")
    
    genai.configure(api_key=gemini_api_key)
    print("API configurada correctamente con la clave proporcionada.")

except Exception as e:
    print(f"Error al configurar la API: {e}")
    raise

def generar_respuesta_historia(prompt):
    """
    Genera respuestas personalizadas para el endpoint de Historia.
    """
    try:
        prompt_historia = f"En contexto histórico LGTBI, responde: {prompt}"
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt_historia)
        if not response or not hasattr(response, 'text'):
            raise ValueError("Respuesta vacía o no válida del modelo.")
        return response.text
    except Exception as e:
        return f"Error al generar respuesta para historia: {str(e)}"
    
def generar_respuesta_recursos(prompt):
    """
    Genera respuestas personalizadas para el endpoint de Recursos.
    """
    prompt_recursos = f"No utilices formato Markdown ni negrita, texto limpio. Sobre recursos LGTBI, responde de manera concisa, aportando enlaces y referencias: {prompt}"
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt_recursos)
        
        if not response or not hasattr(response, 'text'):
            raise ValueError("El modelo no devolvió una respuesta válida.")
        
        return response.text

    except ValueError as ve:
        return f"Error al procesar la respuesta: {str(ve)}"
    except genai.exceptions.GenerativeAiError as ge:
        return f"Error de la API de Gemini: {str(ge)}"
    except Exception as e:
        return f"Error inesperado al generar respuesta: {str(e)}"
    
def generar_respuesta_formacion(prompt):
    """
    Genera respuestas personalizadas para el endpoint de Formación.
    """
    prompt_formacion = f"No utilices formato Markdown ni negrita, texto limpio. Sobre formación en temas LGTBIq+, con una perspectiva pedagógica y accesible, explica u orienta: {prompt}"
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt_formacion)
        
        if not response or not hasattr(response, 'text'):
            raise ValueError("El modelo no devolvió una respuesta válida.")
        
        return response.text

    except ValueError as ve:
        return f"Error: {str(ve)}"
    except genai.exceptions.GenerativeAiError as ge:
        return f"Error de la API de Gemini: {str(ge)}"
    except Exception as e:
        return f"Error inesperado al generar respuesta: {str(e)}"
