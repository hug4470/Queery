# Queer-y 🌈

Queer-y es una aplicación diseñada para proporcionar formación e información relacionada con el colectivo LGTBIQ+, tanto para miembros del colectivo como para personas ajenas que deseen aprender más sobre temas de inclusión, historia, recursos y pedagogía. 🌟

La app está organizada en tres secciones, cada una con un modelo entrenado de forma diferente:

1. **Historia** 🏳️‍🌈: Devuelve datos relevantes sobre la historia del colectivo LGTBIQ+.
2. **Recursos** 📚: Ofrece información sobre cuentas de Instagram, asociaciones y otros recursos útiles para la comunidad.
3. **Formación** 🎓: Explica dudas pedagógicas sobre temas LGTBIQ+ de manera clara y accesible.

Esta aplicación ha sido desarrollada con **Data Engineering**, utilizando tecnologías como **Python**, **AWS**, **Docker** y la **API de Gemini**, además de contar con un **front-end** desarrollado en el primer proyecto de esta índole. 💻💡

---

## Pasos para usarlo ⚙️

### 1. Crear un archivo `.env` local
Para configurar la aplicación, primero necesitas crear un archivo `.env` en la raíz del proyecto con los siguientes datos:

```plaintext
DATABASE_USER=tu_usuario_de_base_de_datos (AWS)
DATABASE_PASSWORD=tu_contraseña_de_base_de_datos (AWS)
DATABASE_HOST=localhost (AWS)
DATABASE_PORT=5432 (AWS)
DATABASE_NAME=nombre_de_tu_base_de_datos (AWS)
GEMINI_API_KEY=tu_clave_api_de_gemini (GeminiAPI)
```

Asegúrate de reemplazar los valores por los correspondientes a tu configuración en AWS y la API de Gemini. 🌐🔑

### 2. Hacer login en Docker 🐳
En la terminal, inicia sesión en Docker para poder acceder a las imágenes del repositorio:

```bash
docker login
```

### 3. Hacer pull de la imagen de DockerHub 📥
Una vez dentro de Docker, realiza el pull de la imagen con el siguiente comando:

```bash
docker pull hugommontes/queery_envless:latest
```

### 4. Ejecutar la imagen con el archivo `.env` 🔄
Asegúrate de estar en la misma carpeta donde se encuentra el archivo `.env` y ejecuta la imagen de Docker con el siguiente comando:

```bash
docker run --env-file .env -p 8000:8000 hugommontes/queery_envless:latest
```

Este comando configura las variables del archivo `.env` y abre el puerto 8000 para que puedas acceder a la aplicación desde tu navegador. 🚀

### 5. Abrir la aplicación en tu navegador 🌍
Finalmente, abre tu navegador y ve a:

```
http://localhost:8000
```

¡Y listo! 🎉

---

## Estructura del Proyecto 🏗️

- **Backend**: El backend está desarrollado en **Python**, utilizando AWS para la base de datos y la API de Gemini para acceder a la información relevante del colectivo LGTBIQ+.
- **Frontend**: El frontend está construido con tecnologías modernas de **HTML**, **CSS** y **JavaScript**. La interfaz está pensada para ser inclusiva, accesible y fácil de usar para todos los usuarios. Aún está en mejoras, es normal si hay aglun aspecto estético que difiera, pero en cuanto a uso debería ser funcional.

---

## Tecnologías utilizadas 🛠️

- **Python**: Para la lógica de backend y procesamiento de datos.
- **AWS**: Para el almacenamiento y gestión de la base de datos.
- **Docker**: Para crear contenedores que faciliten el despliegue de la aplicación.
- **Gemini API**: Para acceder a recursos relacionados con el colectivo LGTBIQ+.
- **HTML/CSS/JS**: Para el desarrollo del frontend.

---

## Contribuye 🤝

No dudes en abrir un issue si encuentras algún problema o tienes sugerencias.

---

¡Queery es para todos! 🏳️‍🌈💪

---

### English Version:

# Queer-y 🌈

Queer-y is an application designed to provide training and information related to the LGTBIQ+ community, both for members of the community and for those who want to learn more about inclusion, history, resources, and pedagogy. 🌟

The app is organized into three sections, each with a differently trained model:

1. **History** 🏳️‍🌈: Returns relevant data about the history of the LGTBIQ+ community.
2. **Resources** 📚: Offers information about Instagram accounts, associations, and other useful resources for the community.
3. **Training** 🎓: Explains pedagogical doubts about LGTBIQ+ topics in a clear and accessible way.

This application was developed using **Data Engineering**, with technologies such as **Python**, **AWS**, **Docker**, and the **Gemini API**, and features a **front-end** developed in the first version of this project. 💻💡

---

## Steps to use it ⚙️

### 1. Create a local `.env` file
To configure the application, you need to create a `.env` file in the root of the project with the following data:

```plaintext
DATABASE_USER=your_aws_database_user (AWS)
DATABASE_PASSWORD=your_aws_database_password (AWS)
DATABASE_HOST=localhost (AWS)
DATABASE_PORT=5432 (AWS)
DATABASE_NAME=your_aws_database_name (AWS)
GEMINI_API_KEY=your_gemini_api_key (GEMINI API)
```

Make sure to replace the values with your specific AWS and Gemini API credentials. 🌐🔑

### 2. Log in to Docker 🐳
In the terminal, log in to Docker to access the images from the repository:

```bash
docker login
```

### 3. Pull the Docker image 📥
Once logged in, pull the image from DockerHub:

```bash
docker pull hugommontes/queery_envless:latest
```

### 4. Run the image with the `.env` file 🔄
Ensure you are in the same folder as the `.env` file and run the image with the following command:

```bash
docker run --env-file .env -p 8000:8000 hugommontes/queery_envless:latest
```

This command will configure the environment variables and open port 8000 so you can access the app from your browser. 🚀

### 5. Open the app in your browser 🌍
Finally, open your browser and go to:

```
http://localhost:8000
```

And you're all set! 🎉

---

## Project Structure 🏗️

- **Backend**: The backend is developed in **Python**, using AWS for database storage and the Gemini API for accessing LGTBIQ+ related information.
- **Frontend**: The frontend is built with modern **HTML**, **CSS**, and **JavaScript** technologies. The interface is designed to be inclusive, accessible, and easy to use for all users.

---

## Technologies Used 🛠️

- **Python**: For backend logic and data processing.
- **AWS**: For database storage and management.
- **Docker**: For containerizing the application.
- **Gemini API**: For accessing LGTBIQ+ related resources.
- **HTML/CSS/JS**: For frontend development.

---

## Contribute 🤝

Feel free to open an issue if you encounter any problems or have suggestions.

---

Queery is for everyone! 🏳️‍🌈💪

