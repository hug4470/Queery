import google.generativeai as genai

# Configurar la clave API
genai.configure(api_key="YOUR_API_KEY")

def generar_respuesta_historia(prompt):
    """
    Genera respuestas personalizadas para el endpoint de Historia.
    """
    prompt_historia = f"En contexto histórico LGTBI, responde: {prompt}"
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt_historia)
        if not response or not hasattr(response, 'text'):
            raise ValueError("Respuesta vacía o no válida del modelo.")
        return response.text
    except ValueError as ve:
        return f"Error: {str(ve)}"
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
        if not response or not hasattr(response, 'text'):
            raise ValueError("Respuesta vacía o no válida del modelo.")
        return response.text
    except ValueError as ve:
        return f"Error: {str(ve)}"
    except Exception as e:
        return f"Error al generar respuesta para recursos: {str(e)}"

def generar_respuesta_formacion(prompt):
    """
    Genera respuestas personalizadas para el endpoint de Formación.
    """
    prompt_formacion = f"Ofrece una explicación educativa: {prompt}"
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt_formacion)
        if not response or not hasattr(response, 'text'):
            raise ValueError("Respuesta vacía o no válida del modelo.")
        return response.text
    except ValueError as ve:
        return f"Error: {str(ve)}"
    except Exception as e:
        return f"Error al generar respuesta para formación: {str(e)}"