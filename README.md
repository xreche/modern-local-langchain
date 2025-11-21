# Modern Local LangChain

Master Modern LangChain (LCEL) with Local LLMs using Ollama. A production-ready guide to building offline AI apps, RAG, and Agents without OpenAI keys. 100% Privacy-focused.

## Tabla de Contenidos

- [Características](#características)
- [Instalación](#instalación)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Notebooks de Aprendizaje](#notebooks-de-aprendizaje)
- [Uso](#uso)
- [Diagnóstico del Entorno](#diagnóstico-del-entorno)
- [Contribuir](#contribuir)
- [Licencia](#licencia)

## Características

- ✅ **100% Local**: Todo se ejecuta en tu máquina, sin APIs externas
- ✅ **LCEL Moderno**: Usa LangChain Expression Language (sintaxis moderna)
- ✅ **Modelos Locales**: Ollama + HuggingFace Embeddings
- ✅ **RAG Completo**: Sistema de Retrieval-Augmented Generation
- ✅ **Agentes Inteligentes**: Agentes con herramientas y razonamiento
- ✅ **Memoria Conversacional**: Gestión de estado y contexto
- ✅ **Privacidad Total**: Tus datos nunca salen de tu computadora

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
│   └── .gitkeep
├── notebooks/               # Jupyter notebooks con ejemplos
│   ├── 00_environment_test.ipynb
│   ├── 01_lcel_fundamentals.ipynb
│   ├── 02_local_rag.ipynb
│   ├── 02_simple_rag.ipynb
│   ├── 03_conversational_memory.ipynb
│   └── 04_local_agents.ipynb
├── src/                     # Código fuente del proyecto
│   ├── __init__.py
│   ├── config.py           # Configuraciones globales
│   └── models.py           # Funciones para instanciar modelos
├── .gitignore
├── requirements.txt
├── setup_doctor.py          # Script de diagnóstico del entorno
└── README.md
```

## Notebooks de Aprendizaje

El proyecto incluye una serie de notebooks progresivos que te enseñan desde lo básico hasta conceptos avanzados:

### 00_environment_test.ipynb
Verificación del entorno de desarrollo. Confirma que todas las dependencias están instaladas correctamente.

### 01_lcel_fundamentals.ipynb
**Fundamentos de LCEL (LangChain Expression Language)**
- Introducción a LCEL y por qué sustituye a las Chains antiguas
- Modelos (The Runnable)
- Prompts con ChatPromptTemplate
- Output Parsers
- El operador Pipe (`|`) - La magia de LCEL
- Ejercicios prácticos

### 02_local_rag.ipynb
**RAG Local: Chat con Documentos 100% Local**
- Ingesta y división de documentos
- Embeddings y Vector Store con ChromaDB
- El Retriever
- Construcción de la cadena RAG completa con LCEL
- Ejemplos prácticos y ejercicios

### 02_simple_rag.ipynb
**RAG Simple: Pipeline 100% Local**
- Pipeline RAG simplificado paso a paso
- Vector Store persistente
- Ejemplos con política de privacidad
- Razonamiento multi-paso

### 03_conversational_memory.ipynb
**Memoria Conversacional: Gestión de Estado en LCEL**
- Teoría del estado: ¿Por qué los LLMs son stateless?
- Componentes de memoria (ChatMessageHistory, RunnableWithMessageHistory)
- Prompts con historial usando MessagesPlaceholder
- Simulación de conversaciones con seguimiento
- Múltiples sesiones independientes

### 04_local_agents.ipynb
**Agentes Locales: Razonamiento con Herramientas**
- Definición de Tools con decorador `@tool`
- Importancia de los docstrings
- Binding de tools al modelo
- Construcción de agentes con `create_tool_calling_agent`
- AgentExecutor y bucle de razonamiento
- Razonamiento multi-paso con múltiples herramientas

## Uso

### Importar Modelos Locales

```python
from src.models import get_local_llm, get_local_embeddings

# Obtener instancia del LLM
llm = get_local_llm()

# Obtener instancia de embeddings
embeddings = get_local_embeddings()
```

### Configuración

Puedes modificar los modelos por defecto en `src/config.py`:

```python
MODEL_NAME = "llama3"  # Modelo LLM de Ollama
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"  # Modelo de embeddings
```

### Ejecutar Notebooks

1. Inicia Jupyter:
```bash
jupyter notebook
```

2. Abre los notebooks en orden (00, 01, 02, etc.) para seguir el aprendizaje progresivo.

## Diagnóstico del Entorno

El proyecto incluye `setup_doctor.py`, un script de diagnóstico que verifica:

- Estado del entorno virtual
- Librerías críticas instaladas
- Disponibilidad de Ollama
- Registro de IPykernel
- Estructura del proyecto

Ejecuta el diagnóstico:

```bash
python setup_doctor.py
```

El script mostrará en colores:
- ✅ Verde: Componentes instalados correctamente
- ❌ Rojo: Componentes faltantes
- ⚠️ Amarillo: Advertencias

## Tecnologías Utilizadas

- **LangChain**: Framework para aplicaciones con LLMs
- **Ollama**: Ejecución local de modelos de lenguaje
- **ChromaDB**: Base de datos vectorial local
- **HuggingFace**: Modelos de embeddings locales
- **Jupyter**: Entorno de desarrollo interactivo

## Requisitos del Sistema

- **Python**: 3.10 o superior
- **RAM**: Mínimo 8GB (recomendado 16GB para modelos grandes)
- **Espacio en disco**: ~5GB para modelos y dependencias
- **Ollama**: Instalado y ejecutándose

## Roadmap

- [ ] Notebook sobre streaming de respuestas
- [ ] Integración con múltiples formatos de documentos (PDF, DOCX)
- [ ] Ejemplos de agentes con RAG
- [ ] Optimizaciones de rendimiento
- [ ] Guía de despliegue en producción

## Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Ver archivo LICENSE para más detalles.

## Autor

Proyecto educativo para aprender LangChain con modelos locales.

---

⭐ Si este proyecto te ha sido útil, considera darle una estrella en GitHub.
