# ------------------ TALLER INTEGRADOR DE PYTHON (UNLZ) ------------------
# CLASE: 
# PROFESOR: GABRIEL NIGLIO
# CUATRIMESTRE: 1ER CUATRIMESTRE
# AÑO: 2025
# 

# ------------------------- [OPERADORES DE IDENTIDAD] -------------------------

'''
Los operadores de identidad comparan si dos variables APUNTAN al mismo objeto en memoria. Esto se aplica a cualquier tipo de variable, aunque en tipos inmutables (como enteros y cadenas) puede haber optimización en caché.

Los operadores son:
- is: Verifica si dos variables apuntan al mismo objeto en memoria.
- is not: Verifica si dos variables NO apuntan al mismo objeto en memoria.

El resultado de esta comparación es un valor BOOLEANO (True o False).
'''

# ------------------------- [EJEMPLOS] -------------------------

# Definimos tres variables
x = [10, 20, 30]  # x es una lista
y = x             # y apunta al mismo objeto que x
z = [10, 20, 30]  # z es un objeto diferente, aunque tiene los mismos valores que x

# Verificamos si x e y apuntan al mismo objeto en memoria
print("x es y:", x is y)  # True (x e y apuntan al mismo objeto)

# Verificamos si x y z apuntan al mismo objeto en memoria
print("x es z:", x is z)  # False (x y z son objetos diferentes en memoria)

# Verificamos si x y z NO apuntan al mismo objeto en memoria
print("x no es z:", x is not z)  # True (x y z son objetos diferentes en memoria)

# ------------------------- [NOTA SOBRE TIPOS INMUTABLES] -------------------------
'''
En tipos inmutables (como enteros o cadenas), Python puede optimizar el uso de memoria reutilizando objetos. Por ejemplo:
'''

a = 100
b = 100
print("a es b (enteros):", a is b)  # True (Python reutiliza el mismo objeto en memoria para enteros pequeños)

c = "Hola"
d = "Hola"
print("c es d (cadenas):", c is d)  # True (Python reutiliza el mismo objeto en memoria para cadenas idénticas)