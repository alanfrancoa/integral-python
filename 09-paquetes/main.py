# ------------------ TALLER INTEGRADOR DE PYTHON (UNLZ) ------------------
# CLASE: 
# PROFESOR: GABRIEL NIGLIO
# CUATRIMESTRE: 1ER CUATRIMESTRE
# AÑO: 2025
# 

# ------------------------- [PAQUETES] -------------------------

'''
Los paquetes son una forma de organizar módulos de manera jerárquica, lo que permite una mayor estructura y organización en proyectos más grandes. Mientras que un módulo es un archivo `.py` que contiene funciones y variables, un paquete es una carpeta que contiene múltiples módulos y un archivo especial llamado `__init__.py`.
'''

# ------------------------- [CREAR UN PAQUETE] -------------------------
'''
Para crear un paquete, seguimos estos pasos:

1. **Crear una carpeta**: Esta carpeta contendrá todos los módulos que formarán parte del paquete. En este caso, creamos una carpeta llamada "paquete".

2. **Archivo `__init__.py`**: Dentro de la carpeta, creamos un archivo llamado `__init__.py`. Este archivo es especial y sirve para indicar que la carpeta es un paquete. No es necesario agregar contenido a este archivo, pero debe existir.

3. **Módulos dentro del paquete**: Dentro de la carpeta, creamos los módulos que necesitemos. Por ejemplo, `herramientas.py` y `pruebas.py`.

La estructura del paquete quedaría así:

paquete/
    __init__.py
    herramientas.py
    pruebas.py
'''

# ------------------------- [IMPORTAR UN PAQUETE] -------------------------
# Ejemplo 1: Importar módulos desde un paquete

# Importamos los módulos `pruebas` y `herramientas` desde el paquete `paquete`
from paquete import pruebas
from paquete import herramientas

# Usamos las funciones de los módulos importados
pruebas.probando()  # Llama a la función `probando()` del módulo `pruebas`
herramientas.nombreCompleto("Sabrina", "Carpenter")  # Llama a la función `nombreCompleto()` del módulo `herramientas`

# ------------------------- [CARPETA __pycache__] -------------------------
'''
Cuando ejecutamos un archivo que importa un paquete, Python genera automáticamente una carpeta llamada `__pycache__` dentro del paquete. Esta carpeta contiene versiones compiladas de los módulos para mejorar el rendimiento. No debemos modificar ni eliminar esta carpeta.
'''

# ------------------------- [PAQUETES EXTERNOS] -------------------------
'''
Además de los paquetes que creamos nosotros, Python permite instalar paquetes externos creados por la comunidad. Estos paquetes se pueden encontrar en el **Python Package Index (PyPI)**, que es un repositorio público de software para Python.

Puedes explorar los paquetes disponibles en: 
https://pypi.org/

Más adelante, veremos cómo instalar y usar paquetes externos en nuestros proyectos.
'''