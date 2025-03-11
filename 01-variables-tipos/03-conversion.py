# ------------------ TALLER INTEGRADOR DE PYTHON (UNLZ) ------------------
# CLASE: 
# PROFESOR: GABRIEL NIGLIO
# CUATRIMESTRE: 1ER CUATRIMESTRE
# AÑO: 2025
# 

# ------------------------- [CONVERTIR DE UN TIPO DE DATO A OTRO] -------------------------

'''
Mencionamos que Python es un lenguaje de programación de tipado DINÁMICO, pero también es un lenguaje cuyo tipado es FUERTE. Esto significa que, aunque no especifiquemos el tipo de dato de una variable, Python no permite ciertas operaciones entre tipos de datos que sean incompatibles sin antes convertirlos.
'''

# Ejemplo de error al concatenar tipos incompatibles
texto = "Hola, mi edad es"
numerito = 10

# print(texto + numerito)  # Esto dará error porque no se puede concatenar un string con un int

# Para poder concatenar un int con un string, debemos convertir el int a string usando la función str()
print(texto + " " + str(numerito))  # Ahora funciona correctamente

# ------------------------- [PASAJE DE TIPOS DE DATOS] -------------------------

'''
Podemos convertir un tipo de dato a otro utilizando funciones como int(), float(), str(), etc. A continuación, se muestra un ejemplo de cómo hacerlo.
'''

# Ejemplo de conversión de tipos de datos
numerito_2 = 99  # Comienza siendo un int
print(numerito_2)
print(type(numerito_2))  # <class 'int'>

# Convertimos el int a float
numerito_2 = float(numerito_2)  
print(numerito_2)
print(type(numerito_2))  # <class 'float'>

# Convertimos el float a string
numerito_2 = str(numerito_2)  
print(numerito_2)
print(type(numerito_2))  # <class 'str'>