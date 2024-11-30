FROM python:3.11-slim

# Crear el directorio de la aplicación
WORKDIR /app

# Copiar el código de la aplicación
COPY . /app

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar el servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]