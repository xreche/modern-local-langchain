#!/usr/bin/env python
"""
Setup Doctor - Diagnóstico del entorno de desarrollo
Verifica el estado del entorno Python y las dependencias críticas.
"""

import sys
import subprocess
import importlib
import shutil
from pathlib import Path

# Colores ANSI para Windows
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def print_header(text):
    """Imprime un encabezado formateado."""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}{text}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.RESET}\n")

def print_success(text):
    """Imprime un mensaje de éxito en verde."""
    print(f"{Colors.GREEN}✓ {text}{Colors.RESET}")

def print_error(text):
    """Imprime un mensaje de error en rojo."""
    print(f"{Colors.RED}✗ {text}{Colors.RESET}")

def print_warning(text):
    """Imprime un mensaje de advertencia en amarillo."""
    print(f"{Colors.YELLOW}⚠ {text}{Colors.RESET}")

def check_virtual_env():
    """Verifica si se está ejecutando en un entorno virtual."""
    print_header("VERIFICACIÓN DE ENTORNO VIRTUAL")
    
    is_venv = sys.prefix != sys.base_prefix
    
    if is_venv:
        print_success(f"Entorno virtual detectado: {sys.prefix}")
    else:
        print_warning("No se detectó un entorno virtual activo")
        print(f"  sys.prefix: {sys.prefix}")
        print(f"  sys.base_prefix: {sys.base_prefix}")
    
    print(f"\nPython version: {sys.version}")
    print(f"Python executable: {sys.executable}")
    
    return is_venv

def check_library(lib_name, import_name=None, version_attr='__version__'):
    """
    Verifica si una librería está instalada e intenta obtener su versión.
    
    Args:
        lib_name: Nombre del paquete para mostrar
        import_name: Nombre para importar (si es diferente de lib_name)
        version_attr: Atributo que contiene la versión
    """
    if import_name is None:
        import_name = lib_name
    
    try:
        module = importlib.import_module(import_name)
        
        # Intentar obtener la versión
        version = "desconocida"
        if hasattr(module, version_attr):
            version = getattr(module, version_attr)
        elif hasattr(module, 'version'):
            version = module.version
        elif hasattr(module, 'VERSION'):
            version = module.VERSION
        
        print_success(f"{lib_name}: versión {version}")
        return True, version
    except ImportError as e:
        print_error(f"{lib_name}: NO INSTALADO - {str(e)}")
        return False, None
    except Exception as e:
        print_error(f"{lib_name}: Error al importar - {str(e)}")
        return False, None

def check_critical_libraries():
    """Verifica las librerías críticas del proyecto."""
    print_header("VERIFICACIÓN DE LIBRERÍAS CRÍTICAS")
    
    libraries = [
        ("langchain", "langchain"),
        ("langchain-community", "langchain_community"),
        ("langchain-core", "langchain_core"),
        ("langchain-text-splitters", "langchain_text_splitters"),
        ("chromadb", "chromadb"),
        ("sentence-transformers", "sentence_transformers"),
        ("jupyter", "jupyter"),
        ("ipykernel", "ipykernel"),
    ]
    
    results = {}
    for lib_name, import_name in libraries:
        installed, version = check_library(lib_name, import_name)
        results[lib_name] = {"installed": installed, "version": version}
    
    return results

def check_ollama_binary():
    """Verifica si el binario de Ollama es accesible."""
    print_header("VERIFICACIÓN DE OLLAMA")
    
    # Verificar si ollama está en PATH
    ollama_path = shutil.which("ollama")
    
    if ollama_path:
        print_success(f"Ollama encontrado en: {ollama_path}")
        
        # Intentar obtener la versión
        try:
            result = subprocess.run(
                ["ollama", "--version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                print_success(f"Versión: {result.stdout.strip()}")
            else:
                print_warning("No se pudo obtener la versión de Ollama")
        except subprocess.TimeoutExpired:
            print_warning("Timeout al verificar versión de Ollama")
        except Exception as e:
            print_warning(f"Error al verificar Ollama: {str(e)}")
        
        return True
    else:
        print_error("Ollama NO encontrado en PATH")
        print_warning("Asegúrate de tener Ollama instalado y en tu PATH")
        return False

def check_ollama_python_package():
    """Verifica si existe el paquete Python de Ollama (opcional)."""
    try:
        import ollama
        print_success(f"Paquete Python 'ollama' encontrado: versión {getattr(ollama, '__version__', 'desconocida')}")
        return True
    except ImportError:
        print_warning("Paquete Python 'ollama' no instalado (opcional, no crítico)")
        return False

def register_ipykernel():
    """Intenta registrar el kernel de ipykernel programáticamente."""
    print_header("REGISTRO DE IPYKERNEL")
    
    try:
        # Verificar si ipykernel está instalado
        import ipykernel
        print_success("ipykernel está instalado")
        
        # Intentar registrar el kernel
        kernel_name = "python3"
        python_exe = sys.executable
        
        # Usar el comando de ipykernel para instalar
        try:
            result = subprocess.run(
                [python_exe, "-m", "ipykernel", "install", "--user", "--name", kernel_name],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                print_success(f"Kernel '{kernel_name}' registrado exitosamente")
                if result.stdout:
                    print(f"  {result.stdout.strip()}")
            else:
                print_warning(f"No se pudo registrar el kernel (puede que ya esté registrado)")
                if result.stderr:
                    print(f"  Error: {result.stderr.strip()}")
        except subprocess.TimeoutExpired:
            print_error("Timeout al registrar el kernel")
        except Exception as e:
            print_warning(f"Error al registrar kernel: {str(e)}")
        
        return True
    except ImportError:
        print_error("ipykernel NO está instalado")
        return False

def check_project_structure():
    """Verifica la estructura básica del proyecto."""
    print_header("VERIFICACIÓN DE ESTRUCTURA DEL PROYECTO")
    
    required_files = [
        "requirements.txt",
        "src/__init__.py",
        "src/config.py",
        "src/models.py",
        "notebooks/00_environment_test.ipynb",
    ]
    
    all_exist = True
    for file_path in required_files:
        path = Path(file_path)
        if path.exists():
            print_success(f"{file_path} existe")
        else:
            print_error(f"{file_path} NO existe")
            all_exist = False
    
    return all_exist

def main():
    """Función principal del diagnóstico."""
    print(f"\n{Colors.BOLD}{Colors.BLUE}")
    print("╔══════════════════════════════════════════════════════════╗")
    print("║         SETUP DOCTOR - Diagnóstico del Entorno           ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print(f"{Colors.RESET}")
    
    # Ejecutar todas las verificaciones
    is_venv = check_virtual_env()
    lib_results = check_critical_libraries()
    ollama_binary = check_ollama_binary()
    ollama_package = check_ollama_python_package()
    kernel_registered = register_ipykernel()
    project_ok = check_project_structure()
    
    # Resumen final
    print_header("RESUMEN FINAL")
    
    critical_missing = [name for name, info in lib_results.items() 
                       if not info["installed"] and name in ["langchain", "chromadb", "sentence-transformers"]]
    
    if critical_missing:
        print_error(f"Librerías críticas faltantes: {', '.join(critical_missing)}")
    else:
        print_success("Todas las librerías críticas están instaladas")
    
    if not ollama_binary:
        print_warning("Ollama no está disponible (necesario para modelos locales)")
    
    if not project_ok:
        print_warning("Algunos archivos del proyecto no existen")
    
    print(f"\n{Colors.BOLD}Diagnóstico completado.{Colors.RESET}\n")
    
    return len(critical_missing) == 0

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Diagnóstico interrumpido por el usuario.{Colors.RESET}")
        sys.exit(1)
    except Exception as e:
        print_error(f"Error inesperado: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

