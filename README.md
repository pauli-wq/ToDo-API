🚀 Características

    Creación de Tareas (To-Do): Agrega nuevas tareas con título, descripción (opcional) y estado de completado.

    Lectura de Tareas: Obtén una lista de todas las tareas o una tarea específica por su ID.

    Actualización de Tareas: Modifica los detalles de una tarea existente.

    Eliminación de Tareas: Borra tareas de la base de datos.

    Validación de Datos: Uso de Pydantic (integrado en SQLModel) para asegurar la integridad de los datos de entrada y salida.

    Base de Datos SQLite: Configuración por defecto para un inicio rápido y fácil.

    Documentación Interactiva: Generación automática de documentación OpenAPI (Swagger UI y ReDoc).

🛠️ Tecnologías Utilizadas

    FastAPI: Framework web moderno y rápido para construir APIs.

    SQLModel: Librería que combina la potencia de SQLAlchemy con la simplicidad de Pydantic para definir modelos de datos y base de datos en un solo lugar.

    Uvicorn: Servidor ASGI de alta velocidad para correr la aplicación FastAPI.

    SQLite: Base de datos ligera utilizada por defecto.

⚙️ Configuración y Ejecución Local

Sigue estos pasos para poner en marcha la API en tu entorno local.

Prerrequisitos

Asegúrate de tener Python 3.8+ instalado en tu sistema.

1. Clona el Repositorio

Clona este repositorio en tu máquina local:

git clone https://github.com/tu_usuario/nombre_del_repositorio.git
cd nombre_del_repositorio

(Nota: Reemplaza tu_usuario/nombre_del_repositorio con la URL real de tu repositorio si ya lo tienes en GitHub.)

2. Crea y Activa un Entorno Virtual (Recomendado)

Es una buena práctica aislar las dependencias de tu proyecto.

python3 -m venv env

Activa el entorno virtual:

    macOS / Linux:

source env/bin/activate

Windows (CMD):

    env\Scripts\activate.bat

Windows (PowerShell):

    env\Scripts\Activate.ps1

3. Instala las Dependencias

Con el entorno virtual activado, instala todas las librerías necesarias:

pip install "fastapi[all]" uvicorn sqlmodel

4. Ejecuta la Aplicación

Una vez instaladas las dependencias, inicia el servidor Uvicorn:

uvicorn main:app --reload

Esto iniciará el servidor en http://127.0.0.1:8000. La opción --reload permite que el servidor se reinicie automáticamente cada vez que detecte cambios en tu código.

🌐 Endpoints de la API y Documentación

Una vez que la aplicación esté corriendo, puedes acceder a la documentación interactiva generada automáticamente por FastAPI.

    Documentación Interactiva (Swagger UI): Abre tu navegador y ve a http://127.0.0.1:8000/docs

    Documentación Alternativa (ReDoc): Abre tu navegador y ve a http://127.0.0.1:8000/redoc

Desde la interfaz de Swagger UI (/docs), puedes probar directamente los endpoints de la API.

Ejemplos de Endpoints:

    POST /todos/: Crea una nueva tarea.

        Cuerpo de la solicitud (JSON):

    {
      "title": "Aprender Docker",
      "description": "Explorar cómo contenerizar la aplicación",
      "completed": false
    }

GET /todos/: Obtiene todas las tareas.

GET /todos/{todo_id}: Obtiene una tarea específica por su ID (ej. /todos/1).

PUT /todos/{todo_id}: Actualiza una tarea existente.

    Cuerpo de la solicitud (JSON):

        {
          "title": "Aprender Docker y K8s",
          "completed": true
        }

DELETE /todos/{todo_id}: Elimina una tarea por su ID (ej. /todos/1).

🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras un error o tienes alguna mejora, no dudes en abrir un issue o enviar un pull request.

📄 Licencia

Este proyecto está bajo la licencia MIT.
