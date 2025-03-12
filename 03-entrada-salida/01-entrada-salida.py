# ------------------ TALLER INTEGRADOR DE PYTHON (UNLZ) ------------------
# CLASE: 
# PROFESOR: GABRIEL NIGLIO
# CUATRIMESTRE: 1ER CUATRIMESTRE
# AÑO: 2025
# 

# ------------------------- [ENTRADA Y SALIDA DE DATOS] -------------------------

'''
Hasta ahora, hemos utilizado la función `print()` para la salida de datos. Sin embargo, también existe una función que nos permite ingresar datos desde el teclado: la función `input()`.

Veamos algunos ejemplos a continuación.
'''

# ------------------------- [EJEMPLO BÁSICO DE INPUT] -------------------------
'''
La función `input()` permite capturar datos ingresados por el usuario. Estos datos siempre se almacenan como cadenas (strings).
'''

# Capturamos el nombre y la edad del usuario
nombre = input("Hola, ¿cuál es tu nombre?: ")
edad = input("¿Cuántos años tienes?: ")

# Mostramos un mensaje de bienvenida con los datos ingresados
print(f"Te doy la bienvenida {nombre}, veo que tienes {edad} años.")

# ------------------------- [MANIPULACIÓN DE VALORES INGRESADOS] -------------------------
'''
A veces necesitamos manipular los valores ingresados, como convertirlos a números para realizar operaciones matemáticas. Veamos un ejemplo.
'''

# Ejemplo: Conversión de temperatura de Celsius a Fahrenheit
celsius = input("Ingresa la temperatura en grados Celsius: ")

# Convertimos el valor ingresado a float para realizar la operación
fahrenheit = (float(celsius) * 9/5) + 32

# Mostramos el resultado de la conversión
print(f"{celsius}°C equivalen a {fahrenheit}°F.")

# ------------------------- [ERROR COMÚN Y SOLUCIÓN] -------------------------
'''
Un error común es intentar realizar operaciones matemáticas con valores ingresados sin convertirlos primero a números. Esto genera un error porque `input()` siempre devuelve un string.
'''

# Ejemplo incorrecto (comentado para evitar errores)
# print(f"El doble de {celsius} es {celsius * 2}")  # Error: No se puede multiplicar un string por un número

# Ejemplo correcto: Convertimos el valor a float antes de operar
print(f"El doble de {celsius} es {float(celsius) * 2}.")
