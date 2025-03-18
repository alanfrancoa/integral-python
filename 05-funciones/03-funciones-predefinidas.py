# ------------------ TALLER INTEGRADOR DE PYTHON (UNLZ) ------------------
# CLASE: 
# PROFESOR: GABRIEL NIGLIO
# CUATRIMESTRE: 1ER CUATRIMESTRE
# AÑO: 2025
# 

# ------------------------- [FUNCIONES PREDEFINIDAS] -------------------------

'''
Python, al igual que otros lenguajes de programación, tiene funciones predefinidas que ya vienen con el lenguaje. Estas funciones son útiles para realizar tareas comunes sin necesidad de escribir código adicional. A continuación, veremos algunas de las funciones más comunes.
'''

# ------------------------- [FUNCIONES DE ENTRADA Y SALIDA] -------------------------
# Ejemplo 1: Funciones `print()` e `input()`

print("¡Bienvenido al taller de Python!")

nombre = input("¿Cómo te llamas? ")
print(f"Hola, {nombre}!")

# ------------------------- [FUNCIÓN `type()`] -------------------------
# Ejemplo 2: Determinar el tipo de dato de una variable

print(type(nombre))  # Salida: <class 'str'>

# ------------------------- [CONVERSIÓN DE TIPOS] -------------------------
# Ejemplo 3: Convertir tipos de datos

edad = "30"
edad_int = int(edad)  # Convertir a entero
print(type(edad_int))  # Salida: <class 'int'>

# ------------------------- [FUNCIÓN `isinstance()`] -------------------------
# Ejemplo 4: Verificar el tipo de dato de una variable

comprobar = isinstance(nombre, str)  # Verificar si `nombre` es de tipo string

if comprobar:
    print("La variable es de tipo string.")
else:
    print("La variable NO es de tipo string.")

# ------------------------- [FUNCIÓN `round()`] -------------------------
# Ejemplo 5: Redondear números decimales

numero = 7.89123
print(round(numero, 2))  # Salida: 7.89 (redondeado a 2 decimales)

# ------------------------- [FUNCIÓN `strip()`] -------------------------
# Ejemplo 6: Eliminar espacios en blanco al inicio y final de un string

frase = "    Python es genial    "
print(frase.strip())  # Salida: "Python es genial"

# ------------------------- [FUNCIONES `upper()` Y `lower()`] -------------------------
# Ejemplo 7: Convertir texto a mayúsculas y minúsculas

texto = "Hola Mundo"
print(texto.upper())  # Salida: "HOLA MUNDO"
print(texto.lower())  # Salida: "hola mundo"

# ------------------------- [FUNCIÓN `split()`] -------------------------
# Ejemplo 8: Dividir un string en una lista

frase = "manzana,banana,cereza"
lista_frutas = frase.split(",")  # Dividir por comas
print(lista_frutas)  # Salida: ['manzana', 'banana', 'cereza']

# ------------------------- [FUNCIÓN `join()`] -------------------------
# Ejemplo 9: Unir una lista de strings en un solo string

frutas = ["manzana", "banana", "cereza"]
fruta_unida = ", ".join(frutas)  # Unir con comas y espacios
print(fruta_unida)  # Salida: "manzana, banana, cereza"

# ------------------------- [FUNCIÓN `find()`] -------------------------
# Ejemplo 10: Encontrar la posición de una subcadena en un string

frase = "El aprendizaje es clave"
posicion = frase.find("clave")
print(posicion)  # Salida: 17 (posición donde comienza "clave")

# ------------------------- [FUNCIONES `max()` Y `min()`] -------------------------
# Ejemplo 11: Encontrar el valor máximo y mínimo en una lista

numeros = [15, 10, 25, 5, 30]
print(max(numeros))  # Salida: 30 (valor máximo)
print(min(numeros))  # Salida: 5 (valor mínimo)

# ------------------------- [FUNCIÓN `sum()`] -------------------------
# Ejemplo 12: Sumar todos los elementos de una lista

suma = sum(numeros)
print(suma)  # Salida: 85 (suma de todos los elementos)

# ------------------------- [FUNCIÓN `sorted()`] -------------------------
# Ejemplo 13: Ordenar una lista

numeros_ordenados = sorted(numeros)
print(numeros_ordenados)  # Salida: [5, 10, 15, 25, 30]

# ------------------------- [CREAR COLECCIONES] -------------------------
# Ejemplo 14: Crear listas, tuplas, conjuntos y diccionarios

mi_lista = list((1, 2, 3))  # Convertir tupla en lista
mi_tupla = tuple([1, 2, 3])  # Convertir lista en tupla
mi_set = set([1, 2, 2, 3])  # Crear conjunto (elimina duplicados)
mi_dict = dict(a=1, b=2)  # Crear diccionario

print(mi_lista)  # Salida: [1, 2, 3]
print(mi_tupla)  # Salida: (1, 2, 3)
print(mi_set)    # Salida: {1, 2, 3}
print(mi_dict)   # Salida: {'a': 1, 'b': 2}

# ------------------------- [FUNCIÓN `map()`] -------------------------
# Ejemplo 15: Aplicar una función a cada elemento de una lista

numeros_2 = [1, 2, 3, 4]
cuadrados = map(lambda x: x**2, numeros_2)  # Elevar al cuadrado
print(list(cuadrados))  # Salida: [1, 4, 9, 16]

# ------------------------- [FUNCIÓN `filter()`] -------------------------
# Ejemplo 16: Filtrar elementos de una lista

numeros_3 = [1, 2, 3, 4, 5, 6]
pares = filter(lambda x: x % 2 == 0, numeros_3)  # Filtrar números pares
print(list(pares))  # Salida: [2, 4, 6]