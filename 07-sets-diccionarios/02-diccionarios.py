# ------------------ TALLER INTEGRADOR DE PYTHON (UNLZ) ------------------
# CLASE: 
# PROFESOR: GABRIEL NIGLIO
# CUATRIMESTRE: 1ER CUATRIMESTRE
# AÑO: 2025
# 

# ------------------------- [DICCIONARIOS] -------------------------

'''
Un diccionario es una estructura de datos que almacena pares de clave-valor. A diferencia de las listas, los diccionarios no tienen un índice numérico, sino que usan claves alfanuméricas (o de cualquier tipo inmutable).

Su similitud, con respecto a otros lenguajes, es con un ARRAY ASOCIATIVO o un OBJETO JSON.
'''

# ------------------------- [DEFINICIÓN DE UN DICCIONARIO] -------------------------
# Ejemplo 1: Definición de un diccionario

disco = {
    "artista": "Lady Gaga",
    "nombre_disco": "Chromatica",
    "año_lanzamiento": 2020,
    "puntaje_metascore": 79,
    "canciones_destacadas": ["Rain on Me", "Stupid Love", "Sour Candy"]
}

print(disco)  # Imprime el diccionario completo
print(type(disco))  # Salida: <class 'dict'>

# ------------------------- [ACCEDER A LOS VALORES DEL DICCIONARIO] -------------------------
# Ejemplo 2: Acceder a valores específicos del diccionario

print("Artista:", disco["artista"])  # Salida: Lady Gaga
print("Nombre del disco:", disco["nombre_disco"])  # Salida: Chromatica
print("Año de lanzamiento:", disco["año_lanzamiento"])  # Salida: 2020
print("Puntaje en MetaScore:", disco["puntaje_metascore"])  # Salida: 79
print("Canciones destacadas:", disco["canciones_destacadas"])  # Salida: ['Rain on Me', 'Stupid Love', 'Sour Candy']

# Acceder a elementos de una lista dentro del diccionario
print("Primera canción destacada:", disco["canciones_destacadas"][0])  # Salida: Rain on Me
print("Segunda canción destacada:", disco["canciones_destacadas"][1])  # Salida: Stupid Love

# ------------------------- [LISTA DE DICCIONARIOS] -------------------------
# Ejemplo 3: Lista de diccionarios

discos_pop = [
    {
        "artista": "Lady Gaga",
        "nombre_disco": "Chromatica",
        "año_lanzamiento": 2020,
        "puntaje_metascore": 79,
        "canciones_destacadas": ["Rain on Me", "Stupid Love", "Sour Candy"]
    },
    {
        "artista": "Dua Lipa",
        "nombre_disco": "Future Nostalgia",
        "año_lanzamiento": 2020,
        "puntaje_metascore": 88,
        "canciones_destacadas": ["Don't Start Now", "Levitating", "Physical"]
    },
    {
        "artista": "Taylor Swift",
        "nombre_disco": "1989",
        "año_lanzamiento": 2014,
        "puntaje_metascore": 76,
        "canciones_destacadas": ["Shake It Off", "Blank Space", "Bad Blood"]
    }
]

# Acceder a un valor específico en la lista de diccionarios
# Supongamos que queremos acceder al puntaje de MetaScore de "Future Nostalgia"
puntaje_future_nostalgia = discos_pop[1]["puntaje_metascore"]
print("Puntaje de 'Future Nostalgia':", puntaje_future_nostalgia)  # Salida: 88

'''
Lo que se hizo fue lo siguiente:
- Primero se accedió al índice del diccionario, en este caso discos_pop[1].
- Una vez que accedí al diccionario, busqué la clave "puntaje_metascore" para obtener su valor.
'''

# ------------------------- [RECORRER LA LISTA DE DICCIONARIOS] -------------------------
# Ejemplo 4: Recorrer la lista de diccionarios

print("---------------------------------")
for disco in discos_pop:
    print(f"Artista: {disco['artista']}")
    print(f"Disco: {disco['nombre_disco']}")
    print(f"Año de lanzamiento: {disco['año_lanzamiento']}")
    print(f"Puntaje en MetaScore: {disco['puntaje_metascore']}")
    print("Canciones destacadas:", ", ".join(disco["canciones_destacadas"]))
    print("---------------------------------")