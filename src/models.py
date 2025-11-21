"""
Funciones para instanciar modelos locales de LangChain.
Incluye funciones para LLM (ChatOllama) y Embeddings (HuggingFace).
"""

from langchain_community.chat_models import ChatOllama
from langchain_community.embeddings import HuggingFaceEmbeddings

from .config import MODEL_NAME, EMBEDDING_MODEL_NAME


def get_local_llm():
    """
    Crea y devuelve una instancia de ChatOllama configurada.
    
    Returns:
        ChatOllama: Instancia del modelo de chat local configurado.
    """
    return ChatOllama(
        model=MODEL_NAME,
        temperature=0.7,
    )


def get_local_embeddings():
    """
    Crea y devuelve una instancia de HuggingFaceEmbeddings configurada.
    
    Returns:
        HuggingFaceEmbeddings: Instancia del modelo de embeddings local configurado.
    """
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL_NAME,
    )

