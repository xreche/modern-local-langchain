# Modern Local LangChain

Master Modern LangChain (LCEL) with Local LLMs using Ollama. A production-ready guide to building offline AI apps, RAG, and Agents without OpenAI keys. 100% Privacy-focused.

## Tabla de Contenidos

<!-- TODO: Agregar enlaces a las secciones del proyecto -->

## Instalación

### Requisitos Previos

- Python 3.10 o superior
- Ollama instalado y ejecutándose localmente
- Modelo LLM descargado en Ollama (por defecto: `llama3`)

### Pasos de Instalación

1. Clona este repositorio:
```bash
git clone <repository-url>
cd modern-local-langchain
```

2. Crea un entorno virtual:
```bash
python -m venv venv
```

3. Activa el entorno virtual:
   - Windows:
   ```bash
   venv\Scripts\activate
   ```
   - Linux/Mac:
   ```bash
   source venv/bin/activate
   ```

4. Instala las dependencias:
```bash
pip install -r requirements.txt
```

5. Verifica la instalación ejecutando el notebook de prueba:
```bash
jupyter notebook notebooks/00_environment_test.ipynb
```

### Configuración de Ollama

Asegúrate de tener Ollama instalado y el modelo configurado descargado:

```bash
# Instalar Ollama (si no lo tienes)
# Visita: https://ollama.ai

# Descargar el modelo por defecto
ollama pull llama3
```

## Estructura del Proyecto

```
modern-local-langchain/
├── data/                    # Directorio para archivos de datos
├── notebooks/               # Jupyter notebooks con ejemplos
│   └── 00_environment_test.ipynb
├── src/                     # Código fuente del proyecto
│   ├── __init__.py
│   ├── config.py           # Configuraciones globales
│   └── models.py           # Funciones para instanciar modelos
├── .gitignore
├── requirements.txt
└── README.md
```

## Uso

### Importar Modelos Locales

```python
from src.models import get_local_llm, get_local_embeddings

# Obtener instancia del LLM
llm = get_local_llm()

# Obtener instancia de embeddings
embeddings = get_local_embeddings()
```

## Contribuir

Las contribuciones son bienvenidas. Por favor, abre un issue o pull request para discutir cambios.

## Licencia

Ver archivo LICENSE para más detalles.
