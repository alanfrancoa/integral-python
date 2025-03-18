# ------------------ TALLER INTEGRADOR DE PYTHON (UNLZ) ------------------
# CLASE: 
# PROFESOR: GABRIEL NIGLIO
# CUATRIMESTRE: 1ER CUATRIMESTRE
# AÑO: 2025
# 

# ------------------------- [FUNCIONES] -------------------------

'''
Una función es un conjunto de instrucciones agrupadas bajo un nombre concreto que pueden reutilizarse invocando a la función tantas veces como sea necesario.

En Python, las funciones tienen la siguiente estructura:

def nombreDeMiFuncion(parametros):
    BLOQUE / CONJUNTO DE INSTRUCCIONES

nombreDeMiFuncion(mi_parametro)
'''

# ------------------------- [FUNCIÓN SIMPLE] -------------------------
# Ejemplo 1: Función sin parámetros

# Definimos una función que imprime nombres de animales
def mostrarAnimales():
    print("Perro")
    print("Gato")
    print("Pájaro")

# Invocamos la función
mostrarAnimales()

# ------------------------- [FUNCIÓN CON PARÁMETROS] -------------------------
# Ejemplo 2: Función con un parámetro

# Definimos una función que recibe un nombre como parámetro
def mostrarNombre(nombre):
    print(f"Tu nombre es: {nombre}")

# Invocamos la función con diferentes nombres
mostrarNombre("Juan")
mostrarNombre("María")
mostrarNombre("Pedro")

# También podemos pedir el nombre al usuario
nombre_usuario = input("Introduce tu nombre: ")
mostrarNombre(nombre_usuario)

# ------------------------- [FUNCIÓN CON MÚLTIPLES PARÁMETROS] -------------------------
# Ejemplo 3: Función con dos parámetros

# Definimos una función que recibe un color y un número
def mostrarColorYNumero(color, numero):
    print(f"El color ingresado es: {color}")

    # Evaluamos si el número está dentro del rango 1 al 10
    if numero < 1 or numero > 10:
        print("ERROR: El número debe estar entre 1 y 10.")
    else:
        print(f"El número ingresado es: {numero}")

# Pedimos al usuario que ingrese un color y un número
color_usuario = input("Introduce un color: ")
numero_usuario = int(input("Introduce un número del 1 al 10: "))

# Invocamos la función
mostrarColorYNumero(color_usuario, numero_usuario)

# ------------------------- [FUNCIÓN CON PARÁMETROS Y BUCLE] -------------------------
# Ejemplo 4: Función que genera una tabla de multiplicar

def tablaMultiplicar(numero):
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):  # Itera del 1 al 10
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Generamos la tabla del 5
tablaMultiplicar(5)

# ------------------------- [USAR FUNCIONES DENTRO DE BUCLES] -------------------------
# Ejemplo 5: Generar tablas de multiplicar del 1 al 10

for num in range(1, 11):  # Itera del 1 al 10
    tablaMultiplicar(num)

# ------------------------- [PARÁMETROS OPCIONALES] -------------------------
# Ejemplo 6: Función con parámetros opcionales

def mostrarUsuario(nombre, edad=None):
    if edad is None:
        print(f"Hola {nombre}, no has proporcionado tu edad.")
    else:
        print(f"Hola {nombre}, tienes {edad} años.")

# Invocamos la función con y sin el parámetro opcional
mostrarUsuario("Carlos", 30)
mostrarUsuario("Ana")

# ------------------------- [USO DEL RETURN] -------------------------
# Ejemplo 7: Función que devuelve un valor

def sumar(a, b):
    return a + b

# Llamamos a la función y guardamos el resultado
resultado_suma = sumar(8, 4)
print("El resultado de la suma es:", resultado_suma)

# ------------------------- [FUNCIONES ANIDADAS] -------------------------
# Ejemplo 8: Funciones dentro de otras funciones

def getNombre(nombre):
    return f"Tu nombre es: {nombre}"

def getEdad(edad):
    return f"Tu edad es: {edad}"

def getNombreYEdad(nombre, edad):
    texto = getNombre(nombre) + "\n" + getEdad(edad)
    return texto

# Llamamos a la función anidada
print(getNombreYEdad("Luis", 25))

# ------------------------- [FUNCIONES LAMBDA] -------------------------
# Ejemplo 9: Función lambda (anónima)

# Definimos una función lambda que devuelve el cuadrado de un número
cuadrado = lambda x: f"El cuadrado de {x} es {x ** 2}"

# Usamos la función lambda
print(cuadrado(5))