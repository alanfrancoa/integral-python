# ------------------ TALLER INTEGRADOR DE PYTHON (UNLZ) ------------------
# CLASE: 
# PROFESOR: GABRIEL NIGLIO
# CUATRIMESTRE: 1ER CUATRIMESTRE
# AÑO: 2025
# 

# ------------------------- [MÓDULO HERRAMIENTAS] -------------------------

'''
Este módulo contiene funciones útiles para manipular y mostrar información. En este caso, la función `nombreCompleto` combina un nombre y un apellido para formar un nombre completo.
'''

# ------------------------- [FUNCIÓN NOMBRECOMPLETO] -------------------------
def nombreCompleto(nombre, apellido):
    '''
    Esta función toma un nombre y un apellido como parámetros y los combina para formar un nombre completo.

    Parámetros:
    - nombre (str): El nombre de la persona.
    - apellido (str): El apellido de la persona.

    Retorna:
    - None: La función no retorna ningún valor, pero imprime el nombre completo en la consola.
    '''
    print(f"{nombre} {apellido}")  # Imprime el nombre completo