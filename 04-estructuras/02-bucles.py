# ------------------ TALLER INTEGRADOR DE PYTHON (UNLZ) ------------------
# CLASE: 
# PROFESOR: GABRIEL NIGLIO
# CUATRIMESTRE: 1ER CUATRIMESTRE
# AÑO: 2025
# 

# ------------------------- [BUCLES] -------------------------

'''
Los bucles son estructuras de control que permiten repetir un bloque de código múltiples veces. Se utilizan para automatizar tareas repetitivas y recorrer estructuras de datos como listas o cadenas.

En Python tenemos dos tipos de bucles:
- WHILE: Se usa cuando no sabemos cuántas veces se repetirá el bucle, pero sí tenemos una condición de parada.
- FOR: Se usa cuando sabemos cuántas veces queremos iterar o cuando recorremos alguna estructura como listas, rangos, etc.
'''

# ------------------------- [BUCLE WHILE] -------------------------
'''
El bucle `while` se ejecuta mientras la condición sea verdadera. Es útil cuando la cantidad de iteraciones no está definida.
'''

# Ejemplo 1: Contador ascendente
contador = 0
while contador < 5:
    print("Contador:", contador)  # Imprime el valor de contador en cada iteración
    contador += 1  # Incremento para evitar un bucle infinito

# ------------------------- [BUCLE FOR] -------------------------
'''
El bucle `for` se usa para iterar sobre una secuencia de valores, como rangos, listas o cadenas.
'''

# Ejemplo 2: Recorrer un rango de números
for i in range(3, 8):  # Itera de 3 a 7
    print("Valor de i:", i)  # Muestra cada número en la secuencia

# Ejemplo 3: Recorrer una lista
frutas = ["manzana", "banana", "naranja", "uva"]
for fruta in frutas:
    print("Fruta:", fruta)  # Muestra cada fruta de la lista

# Ejemplo 4: Recorrer una cadena de texto
palabra = "Hola"
for letra in palabra:
    print("Letra:", letra)  # Muestra cada letra de la palabra "Hola"

# ------------------------- [USO DE BREAK] -------------------------
'''
El uso de `break` permite salir del bucle antes de que la condición deje de ser verdadera.
'''

# Ejemplo 5: Salir del bucle con `break`
i = 0
while i < 10:
    if i == 6:
        break  # Sale del bucle cuando i es 6
    print(i)
    i += 1  # Incremento en cada iteración

# ------------------------- [USO DE CONTINUE] -------------------------
'''
El uso de `continue` salta la iteración actual y continúa con la siguiente sin ejecutar el código restante en esa vuelta.
'''

# Ejemplo 6: Saltar una iteración con `continue`
for i in range(5):
    if i == 3:
        continue  # Omite la impresión cuando i es 3
    print("i:", i)  # Se imprimen todos los valores excepto el 3

# ------------------------- [USO DE ELSE EN BUCLES] -------------------------
'''
El bloque `else` en un bucle se ejecuta solo si el bucle no se interrumpe con un `break`.
'''

# Ejemplo 7: Uso de `else` en un bucle `for`
for i in range(4):
    print("i:", i)
else:
    print("Bucle completado sin interrupciones")  # Se ejecuta si el for finaliza sin interrupciones