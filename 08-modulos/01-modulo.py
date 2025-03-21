# ------------------ TALLER INTEGRADOR DE PYTHON (UNLZ) ------------------
# CLASE: 
# PROFESOR: GABRIEL NIGLIO
# CUATRIMESTRE: 1ER CUATRIMESTRE
# AÑO: 2025
# 

# ------------------------- [MÓDULOS] -------------------------

'''
Los módulos son funcionalidades ya hechas para ser reutilizadas, lo que permite organizar el código en archivos separados para mejorar la mantenibilidad y reutilización.

Para importar un módulo, usamos la siguiente nomenclatura:

import nombre_modulo

Los módulos pueden ser:
- **Estándar**: Los módulos que ya vienen incluidos en Python, como `math`, `os`, `sys`, etc.
- **De terceros**: Se instalan con el comando `pip`, como `numpy`, `pandas`, etc.
- **Personalizados**: Son los archivos `.py` que nosotros mismos creamos.

En Python existen muchos módulos, y se pueden consultar en el siguiente enlace: 
https://docs.python.org/3/library/
'''

# ------------------------- [IMPORTACIÓN DE UN MÓDULO PROPIO] -------------------------
# Importar un módulo personalizado, en este caso "mimodulo.py"
import mimodulo

# Utilización de los métodos del módulo
print(mimodulo.holaMundo("Pepe"))

print(mimodulo.calculadora(20,5, True))
print(mimodulo.calculadora(5,0)) # Recordemos que el tercer parametro es opcioneal 

'''
En el archivo 02-modulo.py veremos otra forma de importar modulos. 
'''