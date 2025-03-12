# ------------------ TALLER INTEGRADOR DE PYTHON (UNLZ) ------------------
# CLASE: 
# PROFESOR: GABRIEL NIGLIO
# CUATRIMESTRE: 1ER CUATRIMESTRE
# AÑO: 2025
# 

# ------------------------- [OPERADORES DE PERTENENCIA] -------------------------

'''
Los operadores de pertenencia verifican si un valor está dentro de una secuencia, como:
- LISTA
- TUPLA
- STRING
- SET
- DICCIONARIO

Los operadores son:
- in: Verifica si un valor está presente en la secuencia.
- not in: Verifica si un valor NO está presente en la secuencia.

El resultado final será un valor BOOLEANO (True o False).
'''

# ------------------------- [LISTA] -------------------------
# Definimos una lista de números
numeros = [10, 20, 30, 40, 50]

# Verificamos si un valor está en la lista
print("20 en lista:", 20 in numeros)  # True (20 está en la lista)

# Verificamos si un valor NO está en la lista
print("99 no en lista:", 99 not in numeros)  # True (99 no está en la lista)

# ------------------------- [STRING] -------------------------
# Definimos un string
texto = "Python es genial"

# Verificamos si un carácter está en el string
print("'e' en texto:", 'e' in texto)  # True ('e' está en el string)

# Verificamos si un carácter NO está en el string
print("'z' no en texto:", 'z' not in texto)  # True ('z' no está en el string)

# ------------------------- [DICCIONARIO] -------------------------
# Definimos un diccionario
mi_diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Buenos Aires"}

# Verificamos si una clave está en el diccionario
print("'edad' en diccionario:", "edad" in mi_diccionario)  # True ('edad' es una clave en el diccionario)

# Verificamos si una clave NO está en el diccionario
print("'profesion' no en diccionario:", "profesion" not in mi_diccionario)  # True ('profesion' no es una clave en el diccionario)