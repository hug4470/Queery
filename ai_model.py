import google.generativeai as genai
import os

try:
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=gemini_api_key)

except:
    print(f"Error: {e}")
    print("Por favor, asegúrate de proporcionar la clave de tu API de Gemini")
    exit()

def generar_respuesta_historia(prompt):
    """
    Genera respuestas personalizadas para el endpoint de Historia.
    """
    try:
        # Construir el prompt para el modelo
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
    prompt_recursos = f"Sobre recursos LGTBI, responde de manera concisa: {prompt}"
    try:
        # Generar respuesta utilizando el modelo de Google Generative AI
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt_recursos)
        
        # Validar la respuesta generada
        if not response or not hasattr(response, 'text'):
            raise ValueError("El modelo no devolvió una respuesta válida.")
        
        return response.text

    except ValueError as ve:
        # Capturar errores de contenido generado
        return f"Error al procesar la respuesta: {str(ve)}"
    except genai.exceptions.GenerativeAiError as ge:
        # Capturar errores específicos de la API de Gemini
        return f"Error de la API de Gemini: {str(ge)}"
    except Exception as e:
        # Capturar cualquier otro error inesperado
        return f"Error inesperado al generar respuesta: {str(e)}"
    
def generar_respuesta_formacion(prompt):
    """
    Genera respuestas personalizadas para el endpoint de Formación.
    """
    prompt_formacion = f"Sobre formación en temas LGTBI, con una perspectiva pedagógica y accesible, como si fueses educador social LGTB+, explica u orienta: {prompt}"
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
