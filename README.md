# Chatbot TFM

Este proyecto implementa un chatbot utilizando ChromaDB como base de datos vectorial y OpenAI para generar embeddings y
respuestas. También incluye un pipeline en Jupyter Notebook para procesar documentos, generar embeddings, y almacenarlos
en la base de datos ChromaDB.

### Estructura del Proyecto

```
.
├── app.py                   # Código principal para ejecutar la aplicación Streamlit
├── Dockerfile               # Configuración del contenedor Docker
├── requirements.txt         # Dependencias necesarias para el proyecto
├── db/                      # Directorio para almacenar la base de datos ChromaDB
│   └── chroma.sqlite3       # Base de datos vectorial generada
├── notebooks/               # Contiene los notebooks Jupyter
│   └── generate_embeddings.ipynb  # Pipeline para procesar y almacenar embeddings
├── services/                # Servicios para gestionar lógica modular
│   ├── chat_handler.py      # Coordinador entre el chatbot y la base de datos
│   ├── openai_service.py    # Gestión de la API de OpenAI
│   └── vector_db_service.py # Gestión de la base de datos vectorial
└── .gitignore               # Archivos y directorios ignorados por Git
```

#### Componentes

1. app.py:
    - Punto de entrada principal de la aplicación Streamlit.
    - Integra los servicios de OpenAI, ChromaDB, y el manejador del chatbot para interactuar con el usuario.
    - La clave API de OpenAI se ingresa directamente en la interfaz de usuario.
2. notebooks/generate_embeddings.ipynb:

    - Pipeline para cargar documentos, generar embeddings con OpenAI, y almacenarlos en ChromaDB.

3. services/:

    - openai_service.py: Maneja la interacción con la API de OpenAI.
    - vector_db_service.py: Interactúa con la base de datos vectorial ChromaDB.
    - chat_handler.py: Gestiona la lógica conversacional, incluyendo la recuperación de documentos y generación de
      respuestas.

4. db/:

    - Almacena la base de datos persistente generada por ChromaDB.
    - Incluye embeddings calculados previamente para optimizar el rendimiento.

### Requisitos Previos

1. Claves API:

    - Necesitas una clave API de OpenAI para generar embeddings y respuestas.
    - La clave se ingresa directamente en la aplicación Streamlit cuando esta se ejecuta.

2. Instalaciones:

    - Python 3.10 o superior.
    - Docker (opcional para ejecutar en un contenedor).

### Configuración del Entorno Local

1. Clona este repositorio:

   ```shell
   git clone <URL del repositorio>
   cd <nombre-del-repositorio>
   ```

2. Instala las dependencias:

   ```shell
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Genera embeddings con el notebook:
    - Abre notebooks/generate_embeddings.ipynb en Jupyter Notebook o Google Colab.
    - Ejecuta las celdas para procesar documentos y guardar los embeddings en la base de datos.

4. Ejecuta la aplicación Streamlit:

   ```shell
   streamlit run app.py
   ```

### Ejecución con Docker

1. Construye la imagen Docker:

```shell
docker build -t streamlit-app .
```

2. Ejecuta el contenedor:

```shell
docker run -p 8501:8501 --name chatbot-container streamlit-app
```

3. Accede a la aplicación:Abre http://localhost:8501 en tu navegador.
