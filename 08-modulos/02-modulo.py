# ------------------ TALLER INTEGRADOR DE PYTHON (UNLZ) ------------------
# CLASE: 
# PROFESOR: GABRIEL NIGLIO
# CUATRIMESTRE: 1ER CUATRIMESTRE
# AÑO: 2025
# 

# ------------------------- [IMPORTACIÓN DE UN MÓDULO - SEGUNDA FORMA] -------------------------

'''
Existe una segunda forma de importar módulos en Python, que nos permite importar funciones específicas o todas las funciones de un módulo directamente.

Sintaxis:
- Para importar todas las funciones: `from nombre_modulo import *`
- Para importar una función específica: `from nombre_modulo import nombre_funcion`
'''

# ------------------------- [IMPORTAR TODAS LAS FUNCIONES DE UN MÓDULO] -------------------------
# Ejemplo 1: Importar todas las funciones de un módulo

# Importamos todas las funciones del módulo "mimodulo"
from mimodulo import *

'''
Con esta forma estamos diciendo: "DESDE el módulo 'mimodulo', quiero que me importes todas las funciones que tiene ese módulo mediante el asterisco (*)".
'''

# Ahora podemos invocar las funciones del módulo de forma directa
print(holaMundo("Jorge"))  # Salida: Hola, ¿qué tal estás, Jorge?
print(calculadora(4, 5, True))  # Salida: Suma: 9 \n Resta: -1
print(calculadora(4, 0))  # Salida: Suma: 4 \n Resta: 4 \n Multiplicación: 0 \n ERROR: No se puede dividir por cero

# ------------------------- [IMPORTAR UNA FUNCIÓN ESPECÍFICA] -------------------------
# Ejemplo 2: Importar una función específica de un módulo

# Importamos solo la función "holaMundo" del módulo "mimodulo"
from mimodulo import holaMundo

# Ahora solo podemos usar la función "holaMundo"
print(holaMundo("Ana"))  # Salida: Hola, ¿qué tal estás, Ana?

# Si intentamos usar otra función, como "calculadora", dará error
# print(calculadora(2, 3))  # Error: NameError: name 'calculadora' is not defined

'''
Esta forma es útil cuando solo necesitamos una o unas pocas funciones de un módulo, evitando cargar funciones innecesarias en memoria.
'''