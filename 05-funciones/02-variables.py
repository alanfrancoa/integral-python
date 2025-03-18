# ------------------ TALLER INTEGRADOR DE PYTHON (UNLZ) ------------------
# CLASE: 
# PROFESOR: GABRIEL NIGLIO
# CUATRIMESTRE: 1ER CUATRIMESTRE
# AÑO: 2025
# 

# ------------------------- [VARIABLES LOCALES Y GLOBALES] -------------------------

'''
En Python, podemos definir dos tipos de variables en el contexto de las funciones:

- **Variables locales**: Son variables que se definen dentro de una función y no se pueden usar fuera de ella. Su ciclo de vida comienza y termina dentro de la función, aunque podemos recuperar su valor si usamos `return`.

- **Variables globales**: Son variables que se declaran fuera de una función y están disponibles tanto dentro como fuera de la función.
'''

# ------------------------- [VARIABLE GLOBAL] -------------------------
# Ejemplo 1: Variable global

# Definimos una variable global
mensaje_global = "¡Bienvenido al taller de Python!"

def mostrarMensajeGlobal():
    print(mensaje_global)  # La variable global es accesible dentro de la función

mostrarMensajeGlobal()  # Salida: ¡Bienvenido al taller de Python!

# ------------------------- [VARIABLE LOCAL] -------------------------
# Ejemplo 2: Variable local

def saludar():
    saludo_local = "Hola, ¿cómo estás?"  # Variable local, solo existe dentro de la función
    print(saludo_local)

saludar()  # Salida: Hola, ¿cómo estás?
# print(saludo_local)  # Error: "saludo_local" no está definida fuera de la función

# ------------------------- [RECUPERAR VALOR DE UNA VARIABLE LOCAL] -------------------------
# Ejemplo 3: Recuperar el valor de una variable local usando `return`

def obtenerFrase():
    frase_local = "Python es increíble"
    return frase_local  # Recuperamos el valor antes de que la variable "muera"

frase_recuperada = obtenerFrase()
print(frase_recuperada)  # Salida: Python es increíble

# ------------------------- [MODIFICAR VARIABLES GLOBALES DENTRO DE UNA FUNCIÓN] -------------------------
# Ejemplo 4: Modificar una variable global dentro de una función

# Definimos una variable global
contador_global = 0

def incrementarContador():
    global contador_global  # Indicamos que estamos usando la variable global
    contador_global += 1  # Modificamos la variable global

incrementarContador()
print(contador_global)  # Salida: 1

# ------------------------- [¿POR QUÉ USAR `global`?] -------------------------
'''
Si no usamos la palabra reservada `global`, Python asumirá que la variable es local dentro de la función, lo que puede causar un error si intentamos modificarla sin haberla inicializado.

Ejemplo incorrecto:
contador = 0

def incrementar():
    contador += 1  # ERROR: UnboundLocalError

incrementar()

En el ejemplo correcto, al usar `global`, le decimos a Python que la variable ya existe en el ámbito global y que no debe crear una nueva variable local.
'''

# ------------------------- [EJEMPLO PRÁCTICO] -------------------------
# Ejemplo 5: Uso de variables globales y locales en un programa

# Variable global
total = 100

def aplicarDescuento(descuento):
    global total  # Usamos la variable global
    total -= descuento  # Aplicamos el descuento al total global

def mostrarTotal():
    print(f"El total después del descuento es: {total}")

# Aplicamos un descuento de 20
aplicarDescuento(20)
mostrarTotal()  # Salida: El total después del descuento es: 80