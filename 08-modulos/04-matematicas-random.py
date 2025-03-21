# ------------------ TALLER INTEGRADOR DE PYTHON (UNLZ) ------------------
# CLASE: 
# PROFESOR: GABRIEL NIGLIO
# CUATRIMESTRE: 1ER CUATRIMESTRE
# AÑO: 2025
# 

# ------------------------- [MÓDULO DE MATEMÁTICAS Y NÚMEROS ALEATORIOS] -------------------------

'''
Python incluye módulos estándar como `math` y `random` que nos permiten realizar operaciones matemáticas avanzadas y generar números aleatorios, respectivamente. A continuación, veremos ejemplos de cómo utilizar estos módulos.
'''

# ------------------------- [MÓDULO MATH] -------------------------
# Ejemplo 1: Importar y usar el módulo `math`

# Importamos todas las funciones y constantes del módulo `math`
from math import *

# Raíz cuadrada
raiz = sqrt(10)  # Calcula la raíz cuadrada de 10
print("Raíz cuadrada de 10:", raiz)  # Salida: 3.1622776601683795

# Constante PI
'''
El módulo `math` incluye constantes matemáticas, como el número PI.
'''
print("Número PI:", pi)  # Salida: 3.141592653589793

# Redondeo
'''
Podemos redondear números hacia arriba o hacia abajo usando las funciones `ceil()` y `floor()`.
'''
print("Redondeo hacia arriba de PI:", ceil(pi))  # Salida: 4 (redondea al entero superior)
print("Redondeo hacia abajo de PI:", floor(pi))  # Salida: 3 (redondea al entero inferior)

# ------------------------- [MÓDULO RANDOM] -------------------------
# Ejemplo 2: Importar y usar el módulo `random`

# Importamos el módulo `random`
import random

# Generar un número aleatorio
'''
El módulo `random` nos permite generar números aleatorios. En este caso, usamos `randint()` para generar un número entero aleatorio dentro de un rango.
'''
numero_aleatorio = random.randint(1, 100)  # Genera un número entre 1 y 100 (ambos incluidos)
print("Número aleatorio entre 1 y 100:", numero_aleatorio)  # Salida: Un número entre 1 y 100