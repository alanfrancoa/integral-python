# ------------------ TALLER INTEGRADOR DE PYTHON (UNLZ) ------------------
# CLASE: 
# PROFESOR: GABRIEL NIGLIO
# CUATRIMESTRE: 1ER CUATRIMESTRE
# AÑO: 2025
# 

# ------------------------- [LISTAS] -------------------------

'''
En capítulos anteriores ya vimos qué es una lista. Para recordar, una LISTA o ARRAY es una estructura de datos en la que una colección o conjunto de datos o valores se encuentran bajo un único nombre.

En esta sección vamos a profundizar más en las listas trabajando en ellas.
'''

# Definir una lista
cds_britney = ["...Baby One More Time", "Oops!... I Did It Again", "Britney", "In the Zone", "Blackout"]

# Las listas no tienen ninguna restricción
detalles_cd = ["Pop", 1999, 4.5, True, "Sony Music"]

print(cds_britney)

'''
En la lista `cds_britney`, cada valor es un ELEMENTO. Donde cada elemento tiene un ÍNDICE que se empieza a contar desde 0.

La lista `cds_britney` tiene 5 elementos donde:

"...Baby One More Time" -> ÍNDICE 0
"Oops!... I Did It Again" -> ÍNDICE 1
"Britney" -> ÍNDICE 2
"In the Zone" -> ÍNDICE 3
"Blackout" -> ÍNDICE 4
'''

# Indices
'''
Para poder acceder a un elemento de una lista en particular, tenemos que tener en cuenta su número de índice y lo hacemos de la siguiente manera.
'''

print(cds_britney[1])  # Salida: "Oops!... I Did It Again"

'''
También podemos seleccionar una cantidad de elementos de la lista especificando un rango desde qué índice hasta qué índice, como vemos a continuación.
'''

print(cds_britney[2:4])  # Salida: ["Britney", "In the Zone"]
'''
Como vemos, solo se incluyeron dos elementos. Debemos tener en cuenta que:

- El primer índice es INCLUSIVO, es decir, se incluye dentro de lo que voy a recuperar de esa lista.
- El segundo índice es EXCLUYENTE, es decir, no se incluirá dentro de la información que se va a recuperar. Este índice solo indica el límite del rango de elementos.
'''

# Modificar un índice
nuevos_lanzamientos = ["Glory", "Circus", "Femme Fatale", "Britney Jean", "Glory (Deluxe)"]

nuevos_lanzamientos[1] = "Circus (Special Edition)"

print(nuevos_lanzamientos)

# Añadir un elemento a la lista
discografia = ["...Baby One More Time", "Oops!... I Did It Again", "Britney", "In the Zone", "Blackout"]

'''
Para añadir un elemento a una lista, debemos utilizar el método `append()`.
'''

discografia.append("Circus")
discografia.append("Femme Fatale")

print(discografia)

# Iterar una lista con un bucle FOR
print("----------- CDs DE BRITNEY SPEARS -----------")

for cd in cds_britney:
    print(f"{cds_britney.index(cd) + 1} - {cd}")

'''
El método `index()` es un método que podemos utilizar en la lista para obtener el índice del elemento. En el bucle, por cada "cd", me va a mostrar su número de índice de la lista y le sumamos 1 para que la lista que se muestra sea más natural.
'''

# Iterando una lista con un bucle WHILE
'''
Vamos a hacer un programa donde vamos a ingresar más CDs de Britney Spears y cuando escriba la palabra "parar", deje de introducir CDs y me muestra la lista.
'''

nuevo_cd = ""

while nuevo_cd != "parar":
    nuevo_cd = input("Introduce un nuevo CD de Britney Spears: ")

    if nuevo_cd != "parar":
        discografia.append(nuevo_cd)

print("----------- DISCOGRAFÍA DE BRITNEY SPEARS -----------")

for cd in discografia:
    print(f"{discografia.index(cd) + 1} - {cd}")

# Listas multidimensionales
'''
Una lista multidimensional puede ocurrir, por ejemplo, cuando tenemos una lista de listas.
'''

detalles_cds = [
    ["...Baby One More Time", 1999],  # ÍNDICE 0
    ["Oops!... I Did It Again", 2000]  # ÍNDICE 1
]

# Acceder a un valor de la lista multidimensional
'''
Supongamos que queremos acceder al valor 1999. Para eso debemos entender lo siguiente:

Primero, tenemos que entender que nuestra lista `detalles_cds` tiene 2 elementos que son sublistas:

detalles_cds[0] → ["...Baby One More Time", 1999]
detalles_cds[1] → ["Oops!... I Did It Again", 2000]

Dentro de `detalles_cds[0]`, el 1999 está en la posición 1.

En resumen:

En la lista `detalles_cds` hay dos sublistas. Primero debemos acceder a la sublista que se encuentra en el ÍNDICE 0.

En dicha sublista, debemos acceder al elemento numérico 1999 que está en el ÍNDICE 1.

El primer índice [0] selecciona la primera lista, y el segundo índice [1] selecciona el número 1999 dentro de ella.
'''

print(detalles_cds[0][1])  # Salida: 1999

# Recorrer esta lista multidimensional
for cd in detalles_cds:  # Recorremos la lista principal
    print(f"CD: {detalles_cds.index(cd) + 1}")
    for dato in cd:  # Recorremos cada elemento dentro de la sublista
        print(f"{dato}")