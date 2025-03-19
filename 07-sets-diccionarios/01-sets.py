# ------------------ TALLER INTEGRADOR DE PYTHON (UNLZ) ------------------
# CLASE: 
# PROFESOR: GABRIEL NIGLIO
# CUATRIMESTRE: 1ER CUATRIMESTRE
# AÑO: 2025
# 

# ------------------------- [SETS] -------------------------

'''
Un set es una estructura de datos similar a las listas, pero con dos diferencias clave:
1. Los sets **no tienen orden**.
2. Los sets **no permiten elementos duplicados**.

Esto significa que los elementos en un set no tienen un índice definido y no se pueden acceder por posición. Además, los elementos se almacenan en un orden aleatorio.
'''

# ------------------------- [DEFINICIÓN DE UN SET] -------------------------
# Ejemplo 1: Definición de un set

discos_lady_gaga = {"The Fame", "Born This Way", "ARTPOP", "Joanne", "Chromatica"}

# Verificamos el tipo de dato
print(type(discos_lady_gaga))  # Salida: <class 'set'>

'''
Como los sets no tienen orden, cada vez que se impriman los elementos, pueden aparecer en un orden diferente.
'''
print(discos_lady_gaga)  # Salida: {"The Fame", "Born This Way", "ARTPOP", "Joanne", "Chromatica"} (orden aleatorio)

# ------------------------- [MÉTODOS DE LOS SETS] -------------------------
# Ejemplo 2: Agregar un elemento al set

# Método add(): Agrega un elemento al set en cualquier posición
discos_lady_gaga.add("The Fame Monster")
print("Set después de add('The Fame Monster'):", discos_lady_gaga)

# Ejemplo 3: Eliminar un elemento del set

# Método remove(): Elimina un elemento específico del set
discos_lady_gaga.remove("ARTPOP")
print("Set después de remove('ARTPOP'):", discos_lady_gaga)

# ------------------------- [OTROS MÉTODOS ÚTILES] -------------------------
# Ejemplo 4: Verificar si un elemento está en el set

# Operador in: Verifica si un elemento está en el set
if "Chromatica" in discos_lady_gaga:
    print("'Chromatica' está en el set.")
else:
    print("'Chromatica' NO está en el set.")

# Ejemplo 5: Unir dos sets

# Método union(): Combina dos sets sin duplicados
nuevos_discos = {"A Star Is Born", "Love for Sale", "Mayhem"}
discografia_completa = discos_lady_gaga.union(nuevos_discos)
print("Discografía completa:", discografia_completa)

# Ejemplo 6: Limpiar un set

# Método clear(): Elimina todos los elementos del set
discos_lady_gaga.clear()
print("Set después de clear():", discos_lady_gaga)  # Salida: set()