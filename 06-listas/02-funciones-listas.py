# ------------------ TALLER INTEGRADOR DE PYTHON (UNLZ) ------------------
# CLASE: 
# PROFESOR: GABRIEL NIGLIO
# CUATRIMESTRE: 1ER CUATRIMESTRE
# AÑO: 2025
# 

# ------------------------- [MÉTODOS DE LISTAS] -------------------------

'''
Las listas en Python tienen métodos propios que nos permiten manipular sus elementos. A continuación, se muestran algunos de los métodos más comunes.
'''

# ------------------------- [CREAR UNA LISTA INICIAL] -------------------------
# Ejemplo 1: Crear una lista inicial
lista_numeros = [10, 20, 30, 40, 50]
print("Lista inicial:", lista_numeros)  # Salida: [10, 20, 30, 40, 50]

# ------------------------- [AGREGAR ELEMENTOS] -------------------------
# Ejemplo 2: Agregar elementos a la lista

# Método append(): Agrega un elemento al final de la lista
lista_numeros.append(60)
print("Lista después de append(60):", lista_numeros)  # Salida: [10, 20, 30, 40, 50, 60]

# Método insert(): Inserta un elemento en una posición específica
lista_numeros.insert(2, 25)  # Inserta 25 en la posición 2
print("Lista después de insert(2, 25):", lista_numeros)  # Salida: [10, 20, 25, 30, 40, 50, 60]

# ------------------------- [ELIMINAR ELEMENTOS] -------------------------
# Ejemplo 3: Eliminar elementos de la lista

# Método remove(): Elimina la primera aparición de un elemento
lista_numeros.remove(30)  # Elimina el número 30
print("Lista después de remove(30):", lista_numeros)  # Salida: [10, 20, 25, 40, 50, 60]

# Método pop(): Elimina y devuelve el último elemento
ultimo_elemento = lista_numeros.pop()
print("Último elemento eliminado:", ultimo_elemento)  # Salida: 60
print("Lista después de pop():", lista_numeros)  # Salida: [10, 20, 25, 40, 50]

# ------------------------- [ORDENAR LISTA] -------------------------
# Ejemplo 4: Ordenar la lista

# Método sort(): Ordena la lista en orden ascendente
lista_numeros.sort()
print("Lista ordenada ascendente:", lista_numeros)  # Salida: [10, 20, 25, 40, 50]

# Método sort(reverse=True): Ordena la lista en orden descendente
lista_numeros.sort(reverse=True)
print("Lista ordenada descendente:", lista_numeros)  # Salida: [50, 40, 25, 20, 10]

# ------------------------- [BUSCAR ELEMENTOS] -------------------------
# Ejemplo 5: Buscar elementos en la lista

# Método index(): Devuelve el índice de un elemento
indice = lista_numeros.index(25)
print("Índice del número 25:", indice)  # Salida: 2

# ------------------------- [CONTAR ELEMENTOS] -------------------------
# Ejemplo 6: Contar elementos en la lista

# Método count(): Cuenta cuántas veces aparece un elemento
cantidad = lista_numeros.count(20)
print("Cantidad de veces que aparece 20:", cantidad)  # Salida: 1

# ------------------------- [COPIAR LISTA] -------------------------
# Ejemplo 7: Copiar una lista

# Método copy(): Crea una copia de la lista
nueva_lista = lista_numeros.copy()
print("Copia de la lista:", nueva_lista)  # Salida: [50, 40, 25, 20, 10]

# ------------------------- [EXTENDER LISTA] -------------------------
# Ejemplo 8: Extender una lista con otra lista

# Método extend(): Agrega elementos de otra lista
lista_numeros.extend([60, 70, 80])
print("Lista después de extend([60, 70, 80]):", lista_numeros)  # Salida: [50, 40, 25, 20, 10, 60, 70, 80]

# ------------------------- [OBTENER SUBLISTA] -------------------------
# Ejemplo 9: Obtener una sublista

# Slicing: Obtener elementos desde el índice 2 hasta el 5 (exclusivo)
sublista = lista_numeros[2:5]
print("Sublista:", sublista)  # Salida: [25, 20, 10]

# ------------------------- [LIMPIAR LISTA] -------------------------
# Ejemplo 10: Limpiar una lista

# Método clear(): Elimina todos los elementos de la lista
lista_numeros.clear()
print("Lista después de clear():", lista_numeros)  # Salida: []