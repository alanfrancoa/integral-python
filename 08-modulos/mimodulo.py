# ------------------ TALLER INTEGRADOR DE PYTHON (UNLZ) ------------------
# CLASE: 
# PROFESOR: GABRIEL NIGLIO
# CUATRIMESTRE: 1ER CUATRIMESTRE
# AÑO: 2025
# 

# ------------------------- [MÓDULO PERSONALIZADO] -------------------------

'''
Los módulos son un conjunto de variables y funciones que podemos utilizar en diferentes partes de nuestro programa. En este caso, vamos a crear un módulo personalizado con dos funciones: una para saludar y otra para realizar operaciones básicas de una calculadora.
'''

# ------------------------- [FUNCIÓN PARA SALUDAR] -------------------------
def holaMundo(nombre):
    '''
    Esta función recibe un nombre como parámetro y devuelve un saludo personalizado.

    Parámetros:
    - nombre (str): El nombre de la persona a saludar.

    Retorna:
    - str: Un mensaje de saludo.
    '''
    return f"Hola, ¿qué tal estás, {nombre}?"

# ------------------------- [FUNCIÓN CALCULADORA] -------------------------
def calculadora(num_1, num_2, basicas=False):
    '''
    Esta función realiza operaciones básicas de una calculadora (suma, resta, multiplicación y división).

    Parámetros:
    - num_1 (float): El primer número.
    - num_2 (float): El segundo número.
    - basicas (bool): Si es True, solo realiza suma y resta. Si es False, que es su valor por default, realiza todas las operaciones.

    Retorna:
    - str: Una cadena con los resultados de las operaciones.
    '''
    suma = num_1 + num_2
    resta = num_1 - num_2
    multiplicacion = num_1 * num_2

    cadena = ""

    if basicas:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
        cadena += "Multiplicación: " + str(multiplicacion)
        cadena += "\n"
        if num_2 == 0:
            cadena += "ERROR: No se puede dividir por cero"
        else:
            division = num_1 / num_2
            cadena += "División: " + str(division)
            cadena += "\n"

    return cadena