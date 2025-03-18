# ------------------ TALLER INTEGRADOR DE PYTHON (UNLZ) ------------------
# CLASE: 
# PROFESOR: GABRIEL NIGLIO
# CUATRIMESTRE: 1ER CUATRIMESTRE
# AÑO: 2025
# 

# ------------------------- [CONDICIONALES] -------------------------

'''
Los condicionales son estructuras que controlan el flujo del programa en base a condiciones. La estructura básica de un `if` en Python es la siguiente:

if se_cumple_esta_condicion:
    Ejecutar grupo de instrucciones
else:
    Ejecutar otro grupo de instrucciones.

Las condiciones se evalúan utilizando OPERADORES DE COMPARACIÓN.
'''

# ------------------------- [IF SIMPLE] -------------------------
# Ejemplo 1: Adivinar la fruta favorita
fruta = input("Adivina cuál es mi fruta favorita: ")

if fruta == "manzana":
    print("¡CORRECTO! Mi fruta favorita es la MANZANA.")
else:
    print("¡Fruta INCORRECTA!")

# ------------------------- [OPERADORES DE COMPARACIÓN] -------------------------
'''
Los operadores de comparación devuelven valores booleanos (True o False), que son útiles para los condicionales.
'''

x = 15
y = 25

print(x < y)  # Menor que: TRUE (x es menor que y)
print(x > y)  # Mayor que: FALSE (x no es mayor que y)
print(x == y) # Igual que: FALSE (x no es igual a y)
print(x != y) # Diferente que: TRUE (x es diferente de y)
print(x <= y) # Menor o igual que: TRUE (x es menor o igual a y)
print(x >= y) # Mayor o igual que: FALSE (x no es mayor o igual a y)

if x < y:
    print("x es menor que y")
else:
    print("x no es menor que y")

# ------------------------- [CONDICIONALES ANIDADOS] -------------------------
'''
Los condicionales anidados evalúan varias condiciones dentro de un mismo bloque. Su estructura es:

if condicion_1:
    # Código que se ejecuta si condicion_1 es True
    if condicion_2:
        # Código que se ejecuta si condicion_2 es True
        if condicion_3:
            # Código que se ejecuta si condicion_3 es True
        else:
            # Código que se ejecuta si condicion_3 es False
    else:
        # Código que se ejecuta si condicion_2 es False
else:
    # Código que se ejecuta si condicion_1 es False
'''

# Ejemplo 2: Condicionales anidados
nombre = "Luna"
animal = "gato"
pais = "España"
edad = 3
adultez = 4

# Primera condición: Verificar si el animal es un gato
if animal == "gato":
    print(f"{nombre} es un gato")

    # Segunda condición (anidada): Verificar si el gato es adulto
    if edad >= adultez:
        print(f"{nombre} es un gato adulto")

        # Tercera condición (anidada): Verificar si el gato es español
        if pais == "España":
            print(f"{nombre} es un gato adulto ESPAÑOL")
        else:
            print(f"{nombre} es un gato adulto pero no es español")
    else:
        print(f"{nombre} NO es un gato adulto")
else:
    print(f"{nombre} NO es un gato")

# ------------------------- [ELIF] -------------------------
'''
El uso de muchos `if` anidados puede dificultar la lectura y mantenimiento del código. Para evaluar múltiples condiciones de manera más clara, se utiliza `elif`. Su estructura es:

if condicion_1:
    bloque de código
elif condicion_2:
    bloque de código
elif condicion_3:
    bloque de código
else:
    bloque de código

Esta estructura es similar a la de `switch` en otros lenguajes, que no existe en Python.
'''

# Ejemplo 3: Uso de `elif` para meses del año
mes = int(input("Introduce un número del 1 al 12 para representar un mes del año: "))

if mes == 1:
    print("Es Enero")
elif mes == 2:
    print("Es Febrero")
elif mes == 3:
    print("Es Marzo")
elif mes == 4:
    print("Es Abril")
elif mes == 5:
    print("Es Mayo")
elif mes == 6:
    print("Es Junio")
elif mes == 7:
    print("Es Julio")
elif mes == 8:
    print("Es Agosto")
elif mes == 9:
    print("Es Septiembre")
elif mes == 10:
    print("Es Octubre")
elif mes == 11:
    print("Es Noviembre")
elif mes == 12:
    print("Es Diciembre")
else:
    print("ERROR: Has ingresado un número inválido.")

# ------------------------- [OPERADORES LÓGICOS Y MÚLTIPLES CONDICIONES] -------------------------
'''
Los operadores lógicos (`and`, `or`, `not`) permiten evaluar múltiples condiciones en un solo `if`.
'''

m = 50
n = 60

# AND: Ambas condiciones deben ser True
if m > 40 and n > 55:
    print("Ambas condiciones son verdaderas, por lo que la condición general es VERDADERA.")

# AND: Una condición es False
if m < 40 and n > 55:
    print("Ambas condiciones son verdaderas, por lo que la condición general es VERDADERA.")
else:
    print("Al menos una condición es falsa, por lo que la condición general es FALSA.")

# OR: Al menos una condición debe ser True
if m > 40 or n < 55:
    print("Al menos una de las condiciones es verdadera, por lo que la condición general es VERDADERA.")

# NOT: Invierte el valor booleano de la condición
if not(m < 40):
    print("El valor booleano ha sido cambiado a TRUE.")