# Usa una imagen base de Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto de la aplicación (por ejemplo, 8000 para FastAPI)
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "main.py"]